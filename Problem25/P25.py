import math

from sympy import fibonacci, log

n = 1
while math.floor(log(fibonacci(n),10)) + 1 < 1000:
    n += 1
print(n)