import time

from sympy import sieve
from sympy.ntheory import totient

start_time = time.time()

def isperm(t, n):
    nperm = [str(n)[i] for i in range(0, len(str(n)))]
    nperm.sort()
    totperm = [str(t)[i] for i in range(0, len(str(t)))]
    totperm.sort()
    if nperm == totperm:
        return 1
    else:
        return 0

minrat = 10
minn = 0
# answer is 2 primes (for large totient) close to sqrt(10**7) multiplied together
primes = [i for i in sieve.primerange(2000, 4000)]
ns = list(set([x*y for x in primes for y in primes if x != y and x*y < 10**7]))
for i in range(0, len(ns)):
    tot = totient(ns[i])
    if isperm(tot, ns[i]) == 1:
        if ns[i] / tot < minrat:
            minrat = ns[i] / tot
            minn = ns[i]
print(minn)

print("--- %s seconds ---" % (time.time() - start_time))