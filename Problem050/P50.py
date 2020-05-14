from sympy import isprime

primes = []
index = 1
while sum(primes) < 1000000:
    if isprime(index):
        primes.append(index)
    index += 1

maxconsecutiveterms = 0
maxsum = 0
for i in range(len(primes) - 1):
    for j in range(len(primes), i, -1):
        if isprime(sum(primes[i:j])) and j - i > maxconsecutiveterms:
            maxsum = sum(primes[i:j])
            maxconsecutiveterms = j - i
            break
print(maxsum)
