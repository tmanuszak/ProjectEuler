from sympy import fibonacci
fiblist = []
x = 0
while fibonacci(x) < 4000001:
    if fibonacci(x) % 2 == 0:
        fiblist.append(fibonacci(x))
    x += 1