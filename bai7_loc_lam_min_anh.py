import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Define kernel_3x3 and kernel_5x5 here
kernel_3x3 = np.ones((3,3), np.float32) / 9.0
kernel_5x5 = np.ones((5,5), np.float32) / 25.0

def apply_filter(kernel):
    global img
    output = cv2.filter2D(img, -1, kernel)
    cv2.imshow('anh lam min', output)

def open_image():
    global img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)
    new_height, new_width = 700, 700
    img = cv2.resize(img, (new_width, new_height))
    cv2.imshow('anh goc', img)

def smooth_image_3x3():
    global img
    output = cv2.filter2D(img, -1, kernel_3x3)
    cv2.imshow('anh lam min 3x3', output)

def smooth_image_5x5():
    global img
    output = cv2.filter2D(img, -1, kernel_5x5)
    cv2.imshow('anh lam min 5x5', output)

root = tk.Tk()
root.title("Ứng dụng Làm Mịn Ảnh")

btn_open = tk.Button(root, text="Mở Ảnh", command=open_image)
btn_open.pack(pady=10)

btn_smooth_3x3 = tk.Button(root, text="Làm mịn 3x3", command=smooth_image_3x3)
btn_smooth_3x3.pack(pady=5)

btn_smooth_5x5 = tk.Button(root, text="Làm mịn 5x5", command=smooth_image_5x5)
btn_smooth_5x5.pack(pady=5)

btn_quit = tk.Button(root, text="Thoát", command=root.quit)
btn_quit.pack(pady=10)

root.mainloop()
