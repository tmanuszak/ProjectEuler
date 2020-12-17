import math

from sympy import isprime

index = 9
flag = False
while flag is False:
    for i in range(math.floor(math.sqrt(index / 2)), 0, -1):
        if isprime(index - 2 * i ** 2):
            break
        elif isprime(index - 2 * i ** 2) is False and i == 1:
            print(index)
            flag = True
    index += 2
    while isprime(index):
        index += 2