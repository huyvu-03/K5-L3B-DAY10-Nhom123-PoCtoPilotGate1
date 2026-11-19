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

- Đức giao phạm vi kiểm kỹ thuật và các giới hạn file trong yêu cầu; quyết định/ngưỡng của bàn và Exit ticket do người điền. Chưa xác nhận nhóm đã đọc lại các kết quả của phiên này.
- Đối chiếu T0–T2: đọc code G0–G3 của Huy, chạy test/eval/gate/trace, bổ sung hồi cứu B6 kỹ thuật và ánh xạ B7.1; ghi S7, C0, C1 phần kỹ thuật, C2. B7.2/B7.3 đã có sẵn; phiên này chạy lại ticket 2 để xác minh, không tự nhận là tác giả nội dung cũ.
- Bổ sung carrier_payload_intervention_rate trong monitors.py, ghi ba ô C8 và kiểm grade; chẩn đoán lệch hash do CRLF chỉ bằng đọc/đổi trong bộ nhớ. Không sửa guards/config/file khoá, không checkpoint, không chốt quyết định thay bàn.

- Trong phiên gộp nhánh, soát khác biệt và xử lý xung đột Phiếu B theo yêu cầu của Đức; giữ B3, B6 kỹ thuật, chẩn đoán S7 và bổ sung tham chiếu lần chạy từ nhánh Hằng.
- Hoàn thiện các ô mô tả còn lại của C8 từ monitor/report hiện có; ngưỡng cảnh báo chưa chốt, để bàn quyết. Đức đã đọc và xác nhận nội dung Exit ticket trong cuộc trao đổi trước khi lưu.

- Đợt tăng cường bằng chứng: kiểm ở clone LF riêng, chạy 12 kiểm tra monitor và bốn ca tự viết × năm seed × hai stage; bổ sung B7.3, C2/C8, đề xuất cách theo dõi/PIC để bàn quyết. Không thay code cổng của Huy, không chốt prepared/v1/v2.

### Bằng chứng

- Mốc đối chiếu: `895d3fd` ký tiêu chí; `372cbba` B7.2/B7.3 có sẵn; `3e0b325` nhận S7; `ce88646` G0–G3 của Huy. Đây là commit tham chiếu, không nhận là đóng góp mới của Đức.
- T0: `R-base-after-20261119-170212-27dcad` (110/110); S7 base `R-S7-before-20261119-170213-27dcad`, after `R-S7-after-20261119-170214-27dcad` (PII 30 → 0); trace `S7-01@11`, `S7-04@11`, `S7-20@11`, `S7-21@11`, đối chứng `S7-05@11`.
- Grade cũ trong checkout CRLF sau đồng bộ business của thành viên khác (4838138): `R-S7-grade-20261119-170938-66af5e`: monitor ✅, bộ nền 0,5 vs S7 0,875; visible/regression ✅, integrity/criteria ❌ do CRLF; public tests Ran 13 tests ... OK. Phiếu B B6 KT1–KT7/B7.1; Phiếu C C0–C2/C8. Commit hoàn thiện phần kỹ thuật của Đức: `cf560cd`; commit gộp nhánh: `7158364`, `9d2b49d`.

- Kiểm định LF trên source 9d7b534: `R-S7-grade-20261119-173939-9d581d` **PASS-VISIBLE**, integrity/criteria/visible/regression/monitor đều ✅; 13 test OK; ma trận tự viết base 0/20 → after 20/20; 12/12 kiểm tra monitor đạt. Chi tiết và lệnh tái lập tại Phiếu C C8; gói `runs/duc-evidence-20261119-173939.zip` chỉ lưu cục bộ theo .gitignore, cần chuyển kèm hoặc tự chạy lại. Đây không phải prepared/test ẩn.

- Đã đồng bộ checkpoint mới của nhóm tại 2dcd26e, xử lý xung đột do khác xuống dòng để giữ nguyên B0 prepared của Huy và chỉ thêm phụ lục kiểm thử của Đức. Grade LF bổ sung `R-S7-grade-20261119-174526-9d581d`: PASS-VISIBLE, checkpoint hash hợp lệ; taken_at 17:38:19 sau nhận S7 16:46:28 nên không nhận là bằng chứng chuẩn bị trước thẻ.

### Exit ticket

- Một điều học được: Tôi học được rằng lọc các trường được phép gửi hãng chặn được cả PII trong ticket và dữ liệu tự lấy từ DB.
- Một điều còn chưa chắc: Tôi còn chưa chắc cách ghi nhận mốc vòng 1 khi nhóm đã nhận S7 trước khi checkpoint.

## PhungVanThanhCao-2A202603741

### Phần việc phụ trách

Vai: Sản phẩm và kinh doanh.

- Câu 1.1, 1.6 (Phiếu A, mục A1, A4, A5): mục tiêu cấp hệ thống, Bản tiêu chí "Nếu … thì chúng tôi sẽ …", bốn câu soát, hai câu ranh giới đầu ra; ký tiêu chí cùng trưởng nhóm.
- Câu 2.3 (Phiếu B, mục B3): bản đồ dữ liệu và một ví dụ drift.
- Câu 2.9 (Phiếu B, mục B7.4): đặt cổng kinh doanh trong `business` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`), mỗi số kèm một câu lý do.
- Quyết định Gate 1 v1 (Phiếu B, mục B8) và v2 (Phiếu C, mục C12, ba dòng bắt buộc); câu 3.2 (Phiếu C, mục C5: specification).
- File: `config/acceptance_criteria.json`, `config/operating_gates.json` (mục `business`).

### Đóng góp cụ thể

- `config/acceptance_criteria.json`: 5 ngưỡng bắt buộc (`pass_rate_min` 0.96, `pass_k_min` 0.86, ba chỉ số an toàn = 0), `escalation_rate_max` 0.35, `business_ops` (7.000đ/ticket, ROI ≥ 0.5, 0 ca ùn), `stop_condition`, bốn `decision_rule` có thứ tự ưu tiên Dừng > Cải tiến thêm > Thu hẹp > Tiếp tục; ký tiêu chí trước lần `eval` đầu tiên.
- Phiếu A: câu 1.1, 1.5, 1.6 (mục A1, A3, A4, A5): câu tiêu chí "Nếu … thì chúng tôi sẽ …", hai câu ranh giới đầu ra, bốn câu soát, lý do cho `business_ops`, ngày xem lại 2026-11-30.
- Phiếu B: B3 (câu 2.3, bản đồ dữ liệu và drift REFUND-v3 → v4 ngày 2026-12-01); B6 (hai dòng lăng kính kinh doanh); B7.4 và mục `business` trong `config/operating_gates.json` (trần hoàn 1.000.000đ/ngày, ngân sách 1.200đ/ticket, phạm vi `all`, ROI ≥ 0.5); B8 (quyết định v1 = Tiếp tục).
- Phiếu C: câu 3.2 (mục C5, specification cho kênh gửi hãng, thẻ S7).
- TODO: C6 (nhánh kinh doanh của fault tree), C7 nếu cần, C12 (quyết định v2 và ba dòng bắt buộc).
- Dùng AI (Claude) để đọc `data/world.json`, `lab10/ops.py` và soạn nháp; mọi ngưỡng đã được bàn rà lại và tự giải thích được.

### Bằng chứng

- Commit ký tiêu chí: `895d3fd` (2026-11-19T16:21), hash tiêu chí `6da9d87f`, trước lần `eval` đầu tiên (16:26).
- Commit liên quan: `4838138` (B7.4, `business`), `6e2f3a7` (B8, quyết định v1), `f1ea39f` (A5).
- Mã lần chạy: base `R-base-before-20261119-162624-90f784`; prepared `R-base-prepared-20261119-173827-51dc56` (hash chốt vòng 1 `7f691dab`).
- Dòng trong phiếu: A1 (câu 1.1), A3, A4, A5; B3, B6 (dòng kinh doanh), B7.4, B8; C5 (câu 3.2).

### Exit ticket

TODO: một điều học được, một điều còn chưa chắc.

## VuQuangHuy-2A202603782

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
