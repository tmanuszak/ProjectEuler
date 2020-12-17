from sympy import prime

n = 1
number = 1
while number < 500000:
    number *= prime(n)
    n += 1
print(number)