import numpy as np
n = int(input("Enter the size of the square matrix: "))
lm=0
tol=0.001
a= np.ones((n, n))
print("Enter the matrix elements:")
for i in range(n):
    for j in range(n):
        a[i][j] = float(input(f"Element [{i}][{j}]: "))
x=np.ones(n)

while True:
    y=np.dot(a,x)
    lm_new=max(abs(y))
    x=y/lm_new
    if(abs(lm_new-lm)<tol):
        break
    lm=lm_new

print(f"value of lamda",lm_new)
print( f"value of x",x)
print(f"value of y",y)

