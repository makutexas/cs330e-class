def polynomial_creator (a, b, c):
    def polynomial (x):
        return a * x**2 + b * x + c
    return polynomial

p1 = polynomial_creator (2, 3, -1)
print(p1(1))

def make_pretty(func):
    def inner():
        print("decorated ", end="")
        return func()
    return inner

@make_pretty
def ordinary():
    print("ordinary ", end="")

ordinary()