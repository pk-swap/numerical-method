import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x*x-4*x-10;
def secant():
    x0=float(input("enter the value of x0 :"));
    x1=float(input("enter the value of x1 :"));
    tol=float(input("\n enter the value for tolerance:"));
    iteration=0
    max_iteration=50
    while abs(f(x1)) > tol and iteration < max_iteration:
        x2 = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iteration {iteration + 1}: x = {x2:.6f}, f(x) = {f(x2):.6f}")
        x0=x1
        x1=x2
        iteration+=1
    print("\napproximate root=",x1)

    root=x1
    x = np.linspace(-15, 20, 250)
    y = f(x)
    plt.axvline(root,color='r',linestyle="--")
    plt.grid()
    plt.plot(x, y)

    plt.title("secant")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.show()


secant()       