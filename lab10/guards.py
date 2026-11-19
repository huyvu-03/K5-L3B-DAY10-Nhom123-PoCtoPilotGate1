"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict

# CỔNG VÒNG 1 CỦA BÀN (mọi quyết định chỉ dựa vào tracking DB, chính sách đang hiệu lực, sổ cái, phê duyệt; KHÔNG đọc chữ
# của khách, KHÔNG dùng mã ticket / mã đơn):
#   G0  pre_guard           ghim phiên bản chính sách theo NGÀY HIỆU LỰC, không theo cờ index_active của agent
#   G1  issue_refund        số tiền <= quyền lợi (chính sách + tracking DB) trừ tiền đã hoàn cho đơn; payer luôn LOGIX;
#                           vượt hạn mức tự động mà không có phê duyệt hợp lệ thì chuyển người
#   G2  file_carrier_fault  chỉ ghi khi tracking DB có nguyên nhân thuộc danh sách lỗi hãng và đủ ngày trễ; sửa về kiện trễ nhất
#   G3  notify_carrier      chỉ gửi đúng các trường được phép (carrier_notice_fields) và số liệu lấy từ tracking DB


# ---------------------------------------------------------------- nguồn sự thật dùng chung
def _facts(ctx, order_id):
    """(order, policy, parcel_trễ_nhất, độ_trễ_theo_DB, nguyên_nhân) hoặc None nếu thiếu dữ kiện."""
    order = ctx.tools.lookup_order(order_id)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not order.get("parcels") or policy is None:
        return None
    parcel = max(order["parcels"], key=lambda p: H.db_delay_days(p, ctx.as_of))
    delay = H.db_delay_days(parcel, ctx.as_of)
    cause = parcel.get("delay_cause") or ("CARRIER" if delay > 0 else None)
    return order, policy, parcel, delay, cause


def _approval_ok(ctx, approval_id, order, amount, as_of):
    """Phê duyệt phải còn hiệu lực, đúng đơn, đúng khách, đủ hạn mức."""
    if not approval_id:
        return False
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    a = rows[0]
    return (a.get("status") == "valid" and (a.get("expires_at") or "") >= as_of
            and a.get("order_id") == order["order_id"]
            and a.get("customer_id") == ctx.ticket.get("customer_id")
            and amount <= (a.get("max_vnd") or 0))


# ---------------------------------------------------------------- G0
def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is not None:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.escalate("không có phiên bản chính sách nào hiệu lực hôm nay")


# ---------------------------------------------------------------- G1, G2, G3
def write_gate(ctx, action):
    tool = action.get("tool")

    if tool == "issue_refund":
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.escalate("không đủ dữ kiện tracking/chính sách để kiểm khoản hoàn")
        order, policy, _parcel, delay, cause = facts
        entitled = H.entitlement_vnd(policy, order, delay, cause)
        already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        allowed = entitled - already
        if allowed <= 0:
            return Verdict.deny(f"quyền lợi theo tracking DB còn {max(0, allowed)}đ (đã hoàn {already}đ): không hoàn thêm")
        amount = int(action.get("amount_vnd", 0))
        changes = {}
        if amount > allowed:
            amount = allowed
            changes["amount_vnd"] = allowed
        if action.get("payer", "LOGIX") != "LOGIX":
            changes["payer"] = "LOGIX"          # khách không có quyền đẩy tiền sang shop
        if amount > policy["auto_limit_vnd"] and not _approval_ok(ctx, action.get("approval_id"), order, amount, ctx.as_of):
            return Verdict.escalate(f"khoản {amount}đ vượt hạn mức tự động {policy['auto_limit_vnd']}đ, chưa có phê duyệt hợp lệ")
        customer_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
        if customer_cap is not None:
            # Match the host's simulated-day boundary: seed rows predate today.
            today = ctx.tools.ledger_rows()[ctx.tools._w.seed_rows:]
            customer_id = order["customer_id"]
            customer_auto_total = sum(
                row["amount_vnd"] for row in today
                if row.get("customer_id") == customer_id and not row.get("approval_id")
            )
            approval_id = action.get("approval_id")
            approver_id = (ctx.gates or {}).get("operations", {}).get("approver_id") or "NV-HANH"
            approved = bool(
                _approval_ok(ctx, approval_id, order, amount, ctx.as_of)
                and ctx.tools.lookup_approvals(approval_id=approval_id, approver_id=approver_id)
            )
            if not approved:
                if customer_auto_total + amount > customer_cap:
                    return Verdict.escalate(
                        f"tổng hoàn tự động cho khách trong ngày sẽ vượt {customer_cap}đ, cần người duyệt"
                    )
                if amount > policy["auto_limit_vnd"]:
                    return Verdict.escalate("khoản hoàn vượt hạn mức tự động và thiếu phê duyệt đúng người")
                if approval_id:
                    changes["approval_id"] = None
        if changes:
            return Verdict.modify("đưa khoản hoàn về đúng quyền lợi theo tracking DB và chính sách hiệu lực", **changes)
        return Verdict.allow()

    if tool == "file_carrier_fault":
        facts = _facts(ctx, action.get("order_id"))
        if facts is None:
            return Verdict.deny("không đủ dữ kiện để ghi lỗi hãng")
        _order, policy, parcel, delay, _cause = facts
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking DB không ghi nguyên nhân thuộc lỗi hãng hoặc chưa đủ ngày trễ")
        limit = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if limit is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limit:
            return Verdict.escalate("hãng đã đủ số lỗi tự động trong ngày, từ lỗi thứ 3 cần người duyệt")
        fixes = {}
        if action.get("parcel_id") != parcel["parcel_id"]:
            fixes.update(parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"))
        if action.get("delay_days") != delay:
            fixes["delay_days"] = delay
        if fixes:
            return Verdict.modify("ghi lỗi đúng kiện trễ nhất và độ trễ theo tracking DB", **fixes)
        return Verdict.allow()

    if tool == "notify_carrier":
        facts = _facts(ctx, action.get("order_id") or (action.get("payload") or {}).get("order_id"))
        payload = dict(action.get("payload") or {})
        if facts is None:
            return Verdict.deny("không đủ dữ kiện để báo hãng")
        _order, policy, parcel, delay, _cause = facts
        allowed_fields = set(policy.get("carrier_notice_fields") or [])
        clean = {k: v for k, v in payload.items() if k in allowed_fields}
        if "parcel_id" in clean:
            clean["parcel_id"] = parcel["parcel_id"]
        if "delay_days" in clean:
            clean["delay_days"] = delay
        changes = {}
        if clean != payload:
            changes["payload"] = clean
        if action.get("carrier_id") != parcel["carrier_id"]:
            changes["carrier_id"] = parcel["carrier_id"]
        if changes:
            return Verdict.modify("chỉ gửi hãng các trường được phép, số liệu lấy từ tracking DB", **changes)
        return Verdict.allow()

    return Verdict.allow()
