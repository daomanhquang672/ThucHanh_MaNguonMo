import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_random_signal(length=100, amplitude=1):
    return amplitude * np.random.randn(length)

def plot_signal():
    signal = generate_random_signal(length=int(entry_length.get()), amplitude=float(entry_amplitude.get()))

    fig, ax = plt.subplots()
    ax.plot(signal)
    ax.set(title='Random Signal', xlabel='Sample', ylabel='Amplitude')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=3, column=0, padx=5, pady=5)

# Tạo giao diện
root = tk.Tk()
root.title("Xử Lý Tín Hiệu Số")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_length = ttk.Label(frame, text="Độ dài tín hiệu:")
label_length.grid(row=0, column=0, padx=5, pady=5)
entry_length = ttk.Entry(frame)
entry_length.grid(row=0, column=1, padx=5, pady=5)

label_amplitude = ttk.Label(frame, text="Biên độ:")
label_amplitude.grid(row=1, column=0, padx=5, pady=5)
entry_amplitude = ttk.Entry(frame)
entry_amplitude.grid(row=1, column=1, padx=5, pady=5)

btn_plot = ttk.Button(frame, text="Vẽ Đồ Thị", command=plot_signal)
btn_plot.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
