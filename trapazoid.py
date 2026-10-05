import numpy as np
def trapezoid():
        a=0
        b=6
    
        n=1
        h=(b-a)/n
        def f(x):
            return 1/(1+x**2)
        result = h/2 * (f(a) + f(b)) 
        for i in range(1, n):
            result += f(a + i * h)   
    
        result *= h
        print("Approximate integral:", result)

trapezoid()
                

    
