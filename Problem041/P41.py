from itertools import permutations as perm

from sympy import isprime

def calc():
    for i in range(1,10):
        perms = sorted(list(perm('1234567890'[:0 - i], 10 - i)), reverse=True)
        numberstring = ''
        for j in range(len(perms)):
            for k in range(len(perms[j])):
                numberstring += perms[j][k]
            if isprime(int(numberstring)):
                return numberstring
            numberstring = ''
    return 0

print(calc())