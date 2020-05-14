from sympy import primerange, isprime
from itertools import permutations


def ispermutation(number1, number2):
    S1 = set([number1[i] for i in range(len(number1))])
    S2 = set([number2[i] for i in range(len(number2))])
    if S1 == S2:
        return True
    else:
        return False


def ispseudopandigital(number):
    if len(number) == len(set(number[i] for i in range(len(number)))):
        return True
    else:
        return False


primes = [i for i in primerange(1000, 10000)]
for i in range(len(primes) - 1):
    for j in range(i + 1, len(primes)):
        if ispermutation(str(primes[i]), str(primes[j])) and ispermutation(str(primes[j]), str(
                primes[j] + abs(primes[j] - primes[i]))) and (primes[j] + abs(primes[j] - primes[i])) in primes and \
                primes[i] != 1487:
            print(''.join(sorted([str(primes[i]), str(primes[j]), str(primes[j] + abs(primes[j] - primes[i]))])))
