import math
from sympy import primerange
answer = 1
primes = [i for i in primerange(1,20)]
for i in range(len(primes)):
    answer *= primes[i]**math.floor(math.log(20,primes[i]))
print(answer)