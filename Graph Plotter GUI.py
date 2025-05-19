"""
Created on Mon May 19 12:15:44 2025

@author: Kunal Kaushik
"""


import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')  # Force backend compatible with Tkinter
import numpy as np
import matplotlib.pyplot as plt

def plot_graph():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            messagebox.showerror("Input error", "Coefficient 'a' cannot be zero for a quadratic equation.")
            return
        x = np.linspace(-10, 10, 100)
        y = a*x**2 + b*x + c
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.title("Quadratic Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Quadratic Graph Plotter")

tk.Label(root, text="Enter coefficient a:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter coefficient b:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter coefficient c:").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Plot Graph", command=plot_graph).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
