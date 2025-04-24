import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")
    
    iterations = []
    for _ in range(max_iter):
        c = (a + b) / 2.0
        iterations.append([a, b, c, f(c)])
        
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return np.array(iterations)

def plot_bisection(iterations):
    x_vals = iterations[:, 2]
    y_vals = iterations[:, 3]
    
    plt.plot(x_vals, y_vals, 'bo-', label='Root approximation')
    plt.axhline(0, color='k', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method Root Finding Process')
    plt.legend()
    try:
        plt.show()
    except:
        plt.savefig("bisection_plot.png")
        print("Graph saved as 'bisection_plot.png' because it couldn't be displayed.")

if __name__ == "__main__":
    a, b = np.random.uniform(-10, 10, 2)
    while f(a) * f(b) >= 0:
        a, b = np.random.uniform(-10, 10, 2)
    
    iterations = bisection_method(min(a, b), max(a, b))
    print("Iterations:")
    print(iterations)
    plot_bisection(iterations)
