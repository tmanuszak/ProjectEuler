from sympy import isprime

largestAmountOfPrimes = 0
correspondingA = 0
correspondingB = 0
counter = 0
for a in range(-999, 1000):
    for b in [i for i in range(1001) if isprime(i)]:
        n = 0
        while isprime(n ** 2 + a * n + b):
            counter += 1
            n += 1
        if counter > largestAmountOfPrimes:
            largestAmountOfPrimes = counter
            correspondingA = a
            correspondingB = b
        counter = 0
print(correspondingA * correspondingB)
