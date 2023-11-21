import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def tinh_va_ve_do_thi():
    # Lấy bậc và các tham số từ các ô nhập liệu
    bac = int(entry_bac.get())
    params = [float(val) for val in entry_params.get().split(",")]

    # Tìm nghiệm của phương trình
    nghiem = np.roots(params)

    # Hiển thị nghiệm lên giao diện
    label_nghiem.config(text=f'Nghiệm: {nghiem}')

    # Tạo các điểm dữ liệu để vẽ đồ thị
    x = np.linspace(-10, 10, 400)
    y = sum(p * x**i for i, p in enumerate(params))

    # Hiển thị đồ thị
    plt.figure()
    plt.plot(x, y)
    plt.title(f'Phương trình bậc {bac}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Tạo giao diện
root = tk.Tk()
root.title("Phương trình bậc n và các tham số")

label_bac = ttk.Label(root, text="Nhập số bậc của phương trình:")
label_bac.grid(row=0, column=0, padx=5, pady=5)

entry_bac = ttk.Entry(root, width=20)
entry_bac.grid(row=0, column=1, padx=5, pady=5)

label_params = ttk.Label(root, text="Nhập các tham số (phân cách bằng dấu phẩy):")
label_params.grid(row=1, column=0, padx=5, pady=5)

entry_params = ttk.Entry(root, width=40)
entry_params.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

btn_tinh_ve = ttk.Button(root, text="Tính và Vẽ Đồ Thị", command=tinh_va_ve_do_thi)
btn_tinh_ve.grid(row=2, column=0, columnspan=2, pady=10)

label_nghiem = ttk.Label(root, text="Nghiệm:")
label_nghiem.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
