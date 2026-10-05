import numpy as np
def f(x,y):
    return 2 * x**2 * y**2

def laplace():
    n=4
    tol=1e-4
    u=np.zeros((n,n))
    h=1
   
    print("Enter boundary values:")

    # Top boundary
    for j in range(n):
        u[0, j] = float(input(f"Top [{j}]: "))

    # Left boundary
    for i in range(1, n):
        u[i, 0] = float(input(f"Left [{i}]: "))

    # Bottom boundary
    for j in range(1, n):
        u[n-1, j] = float(input(f"Bottom [{j}]: "))

    # Right boundary
    for i in range(1, n-1):
        u[i, n-1] = float(input(f"Right [{i}]: "))

    for k in range(1000):
        max_error = 0
        for i in range(1,n-1):
            for j in range(1,n-1):
                x=j*h
                y=i*h
                old=u[i,j]
                u[i,j]=0.25*(u[i-1,j]+u[i+1,j]+u[i,j-1]+u[i,j+1] -h**2*f(x,y))
            error = abs(u[i, j] - old)

            if error > max_error:
                max_error = error

                
         # Check convergence
        if max_error < tol:
            break

    print("Number of iterations:", k + 1)
    print("\nSolution:")
    print(np.round(u, 4))
    
laplace()
# all values 0
