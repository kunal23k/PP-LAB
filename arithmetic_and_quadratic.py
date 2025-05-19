"""
Created on Mon May 19 12:06:53 2025

@author: Kunal Kaushik
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def arithmetic_operations(a, b):
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b if b != 0 else 'Undefined'}")

def quadratic_equation(a, b, c):
    D = b**2 - 4*a*c
    if D >= 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Roots: {root1}, {root2}")
    else:
        print("Complex roots")

def plot_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.title("Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
arithmetic_operations(10, 5)
quadratic_equation(1, -3, 2)
plot_quadratic(1, -3, 2)
