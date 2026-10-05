import numpy as np
def simpsonThreeEighth():
    a=0      
    b=6       
    n=15
     
    h=(b-a)/n
    
    def f(x):
        return 1/(1+x**2)   
    
    s=f(a)+f(b)
    
    for i in range(1, n):
        x=a+i*h
        if i%3==0:
            s += 2 * f(x)
        else:
            s += 3 * f(x)
    
    result = (3*h / 8) * s
    print("Approximate integral:", result)

simpsonThreeEighth()
