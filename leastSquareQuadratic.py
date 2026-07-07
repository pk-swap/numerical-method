import numpy as np
def leastSquare():
    n=int(input("enter the values:"))
    x=np.zeros(n)
    y=np.zeros(n)
    for i in range(n):
        x[i] = float(input(f"Enter x[{i}]: "))
        y[i] = float(input(f"Enter y[{i}]: "))

        sum_x=np.sum(x)
        sum_y=np.sum(y)
        sum_xy=np.sum(x*y)
        sum_x2=np.sum(x*x)

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    a = (sum_y - b * sum_x) / n
        
    print(f"required equation is : y={a:}+{b:}x")


leastSquare()