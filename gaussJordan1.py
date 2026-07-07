import numpy as np
n = int(input("Enter number of variables: "))

def gaussJordan():
    matrix=np.zeros((n,n+1))

    print("enter elements:")
    for i in range(n):
        for j in range (n+1):
            matrix[i][j]=float(input(f"Element [{i}][{j}]: "))
           
    for i in range(n):
        diag=matrix[i][i]

        for j in range(n+1):
            matrix[i][j] = matrix[i][j] / diag

        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n + 1):
                    matrix[k][j] = matrix[k][j] - factor * matrix[i][j]
    print(matrix)

    for i in range(n):
        print(f"x{i+1} = {matrix[i][n]}")

gaussJordan()
        
        