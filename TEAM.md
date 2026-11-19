# Team

## Thông tin nhóm

- Tên nhóm : Nhom123
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom123-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Vũ Quang Huy | 2A202603782 | Kỹ sư cổng (chính) |             |
|   2 | Nguyễn Minh Đức | 2A202603751 | Kỹ sư cổng (phụ) |             |
|   3 | Phùng Văn Thanh Cao | 2A202603741 | Sản phẩm và kinh doanh |             |
|   4 | Đỗ Thị Thu Hằng | 2A202603840 | Vận hành và pháp lý |             |

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

- `config/acceptance_criteria.json`: 5 ngưỡng bắt buộc (`pass_rate_min` 0.96, `pass_k_min` 0.86, ba chỉ số an toàn = 0), `escalation_rate_max` 0.35, `business_ops` (7.000đ/ticket, ROI ≥ 0.5, 0 ca ùn), `stop_condition`, bốn `decision_rule` có thứ tự ưu tiên Dừng > Cải tiến thêm > Thu hẹp > Tiếp tục.
- Phiếu B: B3, câu 2.3 (bản đồ dữ liệu, drift REFUND-v3 → v4 ngày 2026-12-01).
- TODO: Phiếu A (câu 1.1, 1.5, 1.6), mục `business` (B7.4), quyết định v1 (B8), câu 3.2 (C5), quyết định v2 (C12).


### Bằng chứng

TODO: mã commit ký tiêu chí, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

TODO: một điều học được, một điều còn chưa chắc.
## VuQuangHuy-2A202603782

Đã dùng AI để tổng hợp baseline, kết quả so ngưỡng và trace `T-002@55` vào Phiếu B, mục B0–B2.

### Phần việc phụ trách

Vai: Kỹ sư cổng (chính).

- Câu 2.1: chạy đánh giá mốc `base` và đối chiếu kết quả với tiêu chí đã ký.
- Câu 2.2: trace `T-002` với seed `55`, xác định bước sai đầu tiên và ghi nhận lỗi.
- Câu 2.6: viết 2–3 cổng phòng ngừa trong `lab10/guards.py`; phối hợp chốt bản vòng 1 trước khi sửa tiếp ở vòng 2.
- Chạy các lệnh `eval`, `gate` và `trace`; phối hợp với Kỹ sư cổng phụ khi dò sự cố và cập nhật guard vòng 2.

### Đóng góp cụ thể

TODO: ghi việc đã làm, file đã sửa và các cổng đã viết.

### Bằng chứng

TODO: ghi mã commit, mã lần chạy (`runs/<mã>`) và mục phiếu liên quan.

### Exit ticket

TODO: ghi một điều học được và một điều còn chưa chắc.

## DoThiThuHang-2A202603840

### Phần việc phụ trách

Vai: Vận hành và pháp lý (Người 4).

- Câu 2.4 (Phiếu B, mục B4): lập HAZOP vòng 1, gồm rủi ro kỹ thuật và ngoài kỹ thuật.
- Câu 2.4 (Phiếu B, mục B5): hoàn thiện checklist go-live 9 nhóm việc, ghi bằng chứng và PIC có tên cho từng dòng.
- Câu 2.10 (Phiếu B, mục B7.5–B7.6): điền các cổng `operations` và `legal` trong `config/operating_gates.json`; viết runbook phần 1–3 và mục Giờ cao điểm, bảo đảm số liệu khớp cấu hình.
- Câu 3.1 và 3.7 (Phiếu C, mục C4, C10–C11): lập HAZOP theo thẻ sự cố, cập nhật risk register/checklist, viết runbook phần 4–5.
- Gom và rà soát hồ sơ nộp trong `submission/`, gồm `submission/submission.json`; đối chiếu thành viên, thẻ, quyết định và ba dòng bắt buộc với các phiếu trước khi chạy lệnh thu bài.

### Đóng góp cụ thể

- Hoàn thiện HAZOP vòng 1, checklist go-live 9 nhóm việc, Runbook phần 1–3 và mục Giờ cao điểm trong Phiếu B.
- Điền cổng `operations` và `legal` trong `config/operating_gates.json` theo dữ liệu `ops_limits`, `ops_facts` và `staff` của bộ mock.
- Điền `team` và danh sách thành viên trong `submission/submission.json`; để trống thẻ và quyết định vì nhóm chưa nhận thẻ/chưa có kết quả đánh giá.
- Các mục sự cố ở Phiếu C, kênh trực thật và số liệu từ report vẫn chờ nhóm xác nhận/kiểm chứng.

### Bằng chứng

`config/operating_gates.json`; Phiếu B mục B4, B5, B7.5–B7.6; `submission/submission.json`. Public tests: `Ran 13 tests ... OK`. Chưa có mã commit/run: tiêu chí chưa có lock và chưa chạy eval.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
