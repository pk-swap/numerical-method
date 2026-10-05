def f(x,y,z):

    return z

def g(x,y,z):
    
    return (-x*z**2-y**2)


def shooting():
    x=0
    y=1
    z=0
    n=1
    h=0.2
    for i in range(n):
        k1=h*f(x,y,z)
        l1=h*g(x,y,z)

        k2=h*f(x+h/2,y+k1/2,z+l1/2)
        l2=h*g(x+h/2,y+k1/2,z+l1/2)

        k3=h*f(x+h/2,y+k2/2,z+l2/2)
        l3=h*g(x+h/2,y+k2/2,z+l2/2)

        k4=h*f(x+h,y+k3,z+l3)
        l4=h*g(x+h,y+k3,z+l3)

        y=y+(k1+2*k2+2*k3+k4)/6

        z=z+(l1+2*l2+2*l3+l4)/6
        x=x+h
        print("The value of y at x=",x," is:",y)
        print("The value of z at x=",x," is:",z)

shooting()
