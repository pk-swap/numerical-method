import numpy as np
def simpsonOneThird():
    a=0      
    b=6       
    n=6      
    h=(b-a)/n
    
    def f(x):
        return 1/(1+x**2)   
    
    s=f(a)+f(b)
    
    for i in range(1, n):
        x=a+i*h
        if i%2==0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    
    result = (h / 3) * s
    print("Approximate integral:", result)

simpsonOneThird()
