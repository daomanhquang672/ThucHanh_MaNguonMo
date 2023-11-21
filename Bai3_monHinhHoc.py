import tkinter as tk
from tkinter import ttk

def tinh_dien_tich_va_the_tich():
    # Lấy giá trị chiều dài, chiều rộng và chiều cao từ các ô nhập liệu
    chieu_dai = float(entry_chieu_dai.get())
    chieu_rong = float(entry_chieu_rong.get())
    chieu_cao = float(entry_chieu_cao.get())

    # Tính diện tích và thể tích
    dien_tich = chieu_dai * chieu_rong
    the_tich = chieu_dai * chieu_rong * chieu_cao

    # Hiển thị kết quả lên giao diện
    label_ket_qua.config(text=f'Diện tích: {dien_tich:.2f}, Thể tích: {the_tich:.2f}')

# Tạo giao diện
root = tk.Tk()
root.title("Tính Diện Tích và Thể Tích Hình Hộp Chữ Nhật")
root.geometry("500x500")
label_chieu_dai = ttk.Label(root, text="Chiều Dài:")
label_chieu_dai.grid(row=0, column=0, padx=5, pady=5)

entry_chieu_dai = ttk.Entry(root, width=20)
entry_chieu_dai.grid(row=0, column=1, padx=5, pady=5)

label_chieu_rong = ttk.Label(root, text="Chiều Rộng:")
label_chieu_rong.grid(row=1, column=0, padx=5, pady=5)

entry_chieu_rong = ttk.Entry(root, width=20)
entry_chieu_rong.grid(row=1, column=1, padx=5, pady=5)

label_chieu_cao = ttk.Label(root, text="Chiều Cao:")
label_chieu_cao.grid(row=2, column=0, padx=5, pady=5)

entry_chieu_cao = ttk.Entry(root, width=20)
entry_chieu_cao.grid(row=2, column=1, padx=5, pady=5)

btn_tinh = ttk.Button(root, text="Tính Diện Tích và Thể Tích", command=tinh_dien_tich_va_the_tich)
btn_tinh.grid(row=3, column=0, columnspan=2, pady=10)

label_ket_qua = ttk.Label(root, text="Kết Quả:")
label_ket_qua.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
