print("Funct f")
def f(j):
    return lambda i : i + j

y = f(1) # y is pointing at lambda

print(y) 

print(y(2))

print("Func g")
def g(j, k):
    return lambda i: i + j + k

y = g(1, 2)
print(y(3))

print("Func w")
def w(j):
    return lambda i, k:i + j + k

y(1)
y = w(1)
