import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Biến toàn cục để lưu trữ ảnh gốc
original_image = None

def open_image():
    global original_image  # Đảm bảo sử dụng biến toàn cục
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        original_image = cv2.imread(file_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        display_image(original_image)

def display_image(image):
    img = Image.fromarray(image)
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)
    canvas.image = img
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

def apply_edge_detection():
    global original_image  # Đảm bảo sử dụng biến toàn cục
    if original_image is not None:
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray_image, 50, 150)
        display_image(edges)
    else:
        print("Vui lòng chọn ảnh trước khi thực hiện tách biên.")

# Tạo giao diện
root = tk.Tk()
root.title("Chọn Ảnh và Tách Biên")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_open = tk.Button(frame, text="Chọn Ảnh", command=open_image)
btn_open.grid(row=0, column=0, padx=5, pady=5)

btn_detect_edges = tk.Button(frame, text="Tách Biên", command=apply_edge_detection)
btn_detect_edges.grid(row=0, column=1, padx=5, pady=5)

canvas = tk.Canvas(frame, width=300, height=300)
canvas.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
