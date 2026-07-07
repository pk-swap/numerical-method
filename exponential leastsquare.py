import numpy as np

def leastSquare():
    n = int(input("Enter the number of values: "))
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(n):
        x[i] = float(input(f"Enter x[{i}]: "))
        y[i] = float(input(f"Enter y[{i}]: "))
    Y = np.log(y)
    sum_x = np.sum(x)
    sum_Y = np.sum(Y)
    sum_xY = np.sum(x * Y)
    sum_x2 = np.sum(x * x)
    b = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x**2)
    a = (sum_Y - b * sum_x) / n
    A = np.exp(a)
    B=b

    print(f"Required equation is: y = {a:.4f} * e^({b:.4f}x)")

leastSquare()
