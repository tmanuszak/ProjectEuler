import math
from sympy.ntheory.factor_ import digits
print(sum(digits(math.factorial(100))) - 10)