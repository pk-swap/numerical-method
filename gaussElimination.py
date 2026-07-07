import numpy as np
n=int(input("enter the number of variables:"))

def gaussElimination():
    matrix=np.zeros((n,n+1))
    print("enter the augumented matrix:")

    for i in range(n):
        for j in range(n+1):
            matrix[i][j]=float(input(f"elements[{i}][{j}]:"))

    #claculating lower matrix
    for i in range(n):
        maxRow=i
        for k in range(i+1,n):
            if(abs(matrix[k][i])>abs(matrix[maxRow][i])):
                maxRow=k
        matrix[[i, maxRow]] = matrix[[maxRow, i]]

        for j in range(i+1,n):
            matrix[j]=matrix[j]-(matrix[j][i]/matrix[i][i])*matrix[i]   

    print("\nFinal Augmented Matrix:")
    print(matrix)

    #calculating upper matrix
    x=np.zeros(n)
    x[n-1]=matrix[n-1][n]/matrix[n-1][n-1]
    for i in range(n-2,-1,-1):
        sum=0
        for j in range(i+1,n):
            sum=sum+matrix[i][j]*x[j]
        x[i]=(matrix[i][n]-sum)/matrix[i][i]
    print(x)

gaussElimination()




























