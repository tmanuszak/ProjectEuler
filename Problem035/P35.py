from sympy import isprime

circularPrimes = []


def rotate(input, d):
    # slice string in two parts for left and right
    Lfirst = input[0: d]
    Lsecond = input[d:]

    # now concatenate two parts together
    return int(Lsecond + Lfirst)


for i in range(2, 1000000):
    if i not in circularPrimes:
        M = [rotate(str(i), j) for j in range(len(str(i))) if isprime(rotate(str(i), j)) is True]
        if len(M) == len(str(i)):
            circularPrimes.append(M[i] for i in M)

print(len(circularPrimes))
