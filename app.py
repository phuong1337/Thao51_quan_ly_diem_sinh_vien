import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

stt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ten_sv = [
    "Nguyễn Văn An",
    "Trần Thanh Bình",
    "Lê Phương Chi",
    "Phạm Quốc Dũng",
    "Vũ Gia Hà",
    "Hoàng Thảo Lan",
    "Đỗ Hồng Phúc",
    "Bùi Hải Nam",
    "Ngô Nhật Minh",
    "Dương Quỳnh Trang",
]
cc = [8.0, 9.0, 5.0, 9.5, 7.0, 8.5, 4.0, 8.0, 6.0, 9.5]
gk = [7.0, 8.5, 4.0, 9.0, 6.0, 8.5, 4.5, 7.5, 5.5, 9.5]
ck = [7.5, 9.0, 4.5, 9.0, 6.0, 8.7, 4.0, 8.0, 6.0, 9.0]

diem_tong_ket = []
xep_loai_sv = []
for i in range(10):
  tk = round(0.2 * cc[i] + 0.3 * gk[i] + 0.5 * ck[i], 2)
  diem_tong_ket.append(tk)

  if tk >= 8.5:
    xl = "Giỏi"
  elif tk >= 7.0:
    xl = "Khá"
  elif tk >= 5.0:
    xl = "Trung bình"
  else:
    xl = "Yếu"
  xep_loai_sv.append(xl)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.subheader("Bảng điểm chi tiết 10 sinh viên")

df = pd.DataFrame({
    "STT": stt,
    "Họ tên": ten_sv,
    "Chuyên cần": cc,
    "Giữa kỳ": gk,
    "Cuối kỳ": ck,
    "Tổng kết": diem_tong_ket,
    "Xếp loại": xep_loai_sv,
})
st.dataframe(
    df.style.format({
        "Chuyên cần": "{:.1f}",
        "Giữa kỳ": "{:.1f}",
        "Cuối kỳ": "{:.1f}",
        "Tổng kết": "{:.2f}",
    }),
    use_container_width=True,
    hide_index=True,
)

st.subheader("Thống kê kết quả chung")
tong_diem = sum(diem_tong_ket)
diem_tb_lop = round(tong_diem / 10, 2)
cao_nhat = max(diem_tong_ket)
thap_nhat = min(diem_tong_ket)
ten_max = ten_sv[diem_tong_ket.index(cao_nhat)]
ten_min = ten_sv[diem_tong_ket.index(thap_nhat)]
so_luong_dat = sum(1 for tk in diem_tong_ket if tk >= 5.0)

st.write(f"Điểm tổng kết trung bình của lớp: {diem_tb_lop}")
st.write(f"Sinh viên có điểm cao nhất:  {ten_max} ({cao_nhat} điểm)")
st.write(f"Sinh viên có điểm thấp nhất: {ten_min} ({thap_nhat} điểm)")
st.write(f"Số lượng sinh viên đạt (>= 5.0 điểm): {so_luong_dat} / 10 bạn")

st.subheader("Tra cứu thông tin sinh viên")
chon_sv = st.selectbox("Chọn tên sinh viên cần xem:", ten_sv)
idx = ten_sv.index(chon_sv)

col1, col2, col3 = st.columns(3)
col1.metric("Chuyên cần", f"{cc[idx]:.1f}")
col2.metric("Giữa kỳ", f"{gk[idx]:.1f}")
col3.metric("Cuối kỳ", f"{ck[idx]:.1f}")
st.write(f"Điểm tổng kết: **{diem_tong_ket[idx]:.2f}**")
st.write(f"Xếp loại: **{xep_loai_sv[idx]}**")

st.subheader("Biểu đồ điểm tổng kết của lớp")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(ten_sv, diem_tong_ket, color="#5B9BD5")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Sinh viên")
ax.set_xlim(0, 10)
ax.grid(axis="x", linestyle="--", alpha=0.7)
st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>Người tạo:"
    " Nguyễn Phương Thảo - MSSV: 001308060060</p>",
    unsafe_allow_html=True,
)