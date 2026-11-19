# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Nhom123
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom123-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 | Nguyễn Minh Đức | 2A202603751 | Kỹ sư cổng (phụ) |             |
|   3 | Phùng Văn Thanh Cao | 2A202603741 | Sản phẩm và kinh doanh |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenMinhDuc-2A202603751

### Phần việc phụ trách

Vai: Kỹ sư cổng (phụ).

- Câu 2.7 (Phiếu B, mục B7.2): hai bước tránh rò rỉ dữ liệu.
- Câu 2.8 (Phiếu B, mục B7.3): behavioral test và hai ticket hiểm chạy bằng `--adhoc`.
- Câu 3.1, 3.6 (Phiếu C, mục C2, C8): dò trace ticket hỏng của thẻ, thêm chỉ số theo dõi.
- File: `lab10/monitors.py` (dict `MONITORS`); cùng Kỹ sư cổng chính sửa `lab10/guards.py` ở vòng 2.

### Đóng góp cụ thể

TODO: điền sau khi làm xong (việc đã làm, file đã sửa, cổng đã viết).

### Bằng chứng

TODO: mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

TODO: một điều học được, một điều còn chưa chắc.

## PhungVanThanhCao-2A202603741

### Phần việc phụ trách

Vai: Sản phẩm và kinh doanh.

- Câu 1.1, 1.6 (Phiếu A, mục A1, A4, A5): mục tiêu cấp hệ thống, Bản tiêu chí "Nếu … thì chúng tôi sẽ …", bốn câu soát, hai câu ranh giới đầu ra; ký tiêu chí cùng trưởng nhóm.
- Câu 2.3 (Phiếu B, mục B3): bản đồ dữ liệu và một ví dụ drift.
- Câu 2.9 (Phiếu B, mục B7.4): đặt cổng kinh doanh trong `business` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`), mỗi số kèm một câu lý do.
- Quyết định Gate 1 v1 (Phiếu B, mục B8) và v2 (Phiếu C, mục C12, ba dòng bắt buộc); câu 3.2 (Phiếu C, mục C5: specification).
- File: `config/acceptance_criteria.json`, `config/operating_gates.json` (mục `business`).

### Đóng góp cụ thể

- `config/acceptance_criteria.json`: 5 ngưỡng bắt buộc (`pass_rate_min` 0.96, `pass_k_min` 0.9, ba chỉ số an toàn = 0), `escalation_rate_max` 0.35, `business_ops` (7.000đ/ticket, ROI ≥ 0.5, 0 ca ùn), `stop_condition`, bốn `decision_rule` có thứ tự ưu tiên Dừng > Cải tiến thêm > Thu hẹp > Tiếp tục.
- Phiếu B: B3, câu 2.3 (bản đồ dữ liệu, drift REFUND-v3 → v4 ngày 2026-12-01).
- TODO: Phiếu A (câu 1.1, 1.5, 1.6), mục `business` (B7.4), quyết định v1 (B8), câu 3.2 (C5), quyết định v2 (C12).


### Bằng chứng

TODO: mã commit ký tiêu chí, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

TODO: một điều học được, một điều còn chưa chắc.
