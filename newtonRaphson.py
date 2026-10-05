import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x*x-4*x-10;
def der(x):
    return 2*x-4;
def newtonsraphson():
    x0=float(input("enter the value of x0 :"));
    tol=float(input("\n enter the value for tolerance:"));

    iteration=0
    max_iteration=50

    while abs(f(x0)) > tol and iteration < max_iteration:
        x1=x0-(f(x0)/der(x0));
        print(f"Iteration {iteration+1}: x = {x1}")
        x0=x1;
        iteration+=1
    print("\napproximate root=",x0)

    root=x0
    x = np.linspace(-15, 20, 250)
    y = f(x)
    plt.axvline(root,color='r',linestyle="--")
    # plt.axhline(root,color='r',linestyle='--')
    plt.grid()
    plt.plot(x, y)

    plt.title("newton raphson method")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.show()

newtonsraphson()