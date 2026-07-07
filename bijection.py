def func(x):
    return x**2 - 5*x - 6   # Function

def bisection(a, b):
    if func(a) * func(b) >= 0:
        print("No solution")
        return None

   
    print("Iteration\t a\t\t b\t\t m\t\t f(a)\t\t f(m)\t\t f(b)")
    print("-"*80)

    iteration = 1
    while (b - a) > 0.01:   
        m = (a + b) / 2
        print(f"{iteration}\t\t {a:.4f}\t {b:.4f}\t {m:.4f}\t {func(a):.4f}\t {func(m):.4f}\t {func(b):.4f}")

        if func(m) == 0:
            return m
        elif func(a) * func(m) < 0:
            b = m
        else:
            a = m
        iteration += 1

    return (a + b) / 2


a = float(input("Enter a: "))
b = float(input("Enter b: "))

bisection(a, b)
