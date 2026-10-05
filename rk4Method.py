import numpy as np
def f(x,y):
    return ((y**2-x**2)/(y**2+x**2))

def rk4Method(f,x0,y0,x1,n):
    x=x0
    y=y0
    h=(x1-x0)/n

    for i in range(n):
        k1 = h*f(x,y)
        k2 = h*f(x+h/2,y+k1/2)
        k3 = h*f(x+h/2,y+k2/2)
        k4 = h*f(x+h,y+k3)
        y = y+(k1+2*k2 +2*k3 +k4) /6
        x = x + h

    return y
x0 = 0  
y0 = 1  
x1=2
n = 10   

print(f"The value of y at x = {x0} is {y0}")
rk4Method()
