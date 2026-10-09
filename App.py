
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    layout="wide"
)

# 2. Tao du lieu sinh vien
data = {
    "Họ và tên": [
        "Nguyễn Văn An",
        "Trần Thị Thanh Bình",
        "Lê Quốc Cường",
        "Phạm Minh Đức",
        "Võ Ngọc Bích",
        "Đặng Quốc Huy",
        "Bùi Gia Thiều",
        "Hoàng Gia Minh",
        "Đỗ Phương Nam",
        "Nguyễn Bảo Phong"
    ],
    "Điểm chuyên cần": [9, 8, 10, 7, 9, 6, 8, 10, 7, 9],
    "Điểm giữa kỳ": [8, 7, 9, 6, 8, 5, 7, 9, 6, 8],
    "Điểm cuối kỳ": [9, 8, 9, 7, 8, 4, 8, 10, 5, 9]
}

df = pd.DataFrame(data)

# 3. Tinh diem tong ket
df["Tổng kết"] = (
    df["Điểm chuyên cần"] * 0.2
    + df["Điểm giữa kỳ"] * 0.3
    + df["Điểm cuối kỳ"] * 0.5
).round(2)

# 4. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 5. Tieu de trang web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm, thống kê và xếp loại kết quả học tập.")

# 6. Hien thi bang diem
st.subheader("Bảng điểm sinh viên")

st.dataframe(
    df.style.format({"Tổng kết": "{:.2f}"}),
    width="stretch"
)

# 7. Thong ke ket qua hoc tap
st.subheader("Thống kê kết quả học tập")

diem_trung_binh = df["Tổng kết"].mean()
vi_tri_max = df["Tổng kết"].idxmax()
vi_tri_min = df["Tổng kết"].idxmin()

sv_max = df.loc[vi_tri_max]
sv_min = df.loc[vi_tri_min]

so_sv_dat = (df["Tổng kết"] >= 5).sum()

cot1, cot2, cot3 = st.columns(3)

cot1.metric(
    "Điểm trung bình lớp",
    f"{diem_trung_binh:.2f}"
)

cot2.metric(
    "Số sinh viên đạt",
    f"{so_sv_dat}/{len(df)}"
)

cot3.metric(
    "Tổng số sinh viên",
    len(df)
)

st.write(
    f"**Sinh viên có điểm cao nhất:** "
    f"{sv_max['Họ và tên']} - {sv_max['Tổng kết']:.2f} điểm"
)

st.write(
    f"**Sinh viên có điểm thấp nhất:** "
    f"{sv_min['Họ và tên']} - {sv_min['Tổng kết']:.2f} điểm"
)

# 8. Tra cuu diem theo sinh vien
st.subheader("Tra cứu điểm theo sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Họ và tên"].tolist()
)

# Tim dung sinh vien duoc chon
sv = df.loc[df["Họ và tên"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Họ và tên']}")

cot1, cot2, cot3 = st.columns(3)

cot1.metric(
    "Chuyên cần",
    f"{sv['Điểm chuyên cần']:.2f}"
)

cot2.metric(
    "Giữa kỳ",
    f"{sv['Điểm giữa kỳ']:.2f}"
)

cot3.metric(
    "Cuối kỳ",
    f"{sv['Điểm cuối kỳ']:.2f}"
)

cot4, cot5 = st.columns(2)

cot4.metric(
    "Điểm tổng kết",
    f"{sv['Tổng kết']:.2f}"
)

cot5.metric(
    "Xếp loại",
    sv["Xếp loại"]
)

# 9. Ve bieu do cot
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(df["Họ và tên"], df["Tổng kết"])

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 10. Thong tin nguoi tao
st.markdown("---")
st.caption("Người thực hiện: [VŨ THANH KHIẾT ] | MSSV: [001308059802]")
