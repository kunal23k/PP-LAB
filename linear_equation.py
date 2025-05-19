"""
Created on Mon May 19 12:08:54 2025

@author: Kunal Kaushik
"""
import matplotlib.pyplot as plt
import numpy as np

def solve_linear(m, c):
    print(f"Linear Equation: y = {m}x + {c}")

def plot_linear(m, c):
    x = np.linspace(-10, 10, 100)
    y = m*x + c
    plt.plot(x, y, label=f'y = {m}x + {c}', color='green')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Equation Graph")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
solve_linear(2, 3)
plot_linear(2, 3)



