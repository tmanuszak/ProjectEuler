import time
from sympy import sieve

start_time = time.time()

print(sum(list(sieve.totientrange(2,10**6 + 1))))

print("--- %s seconds ---" % (time.time() - start_time))