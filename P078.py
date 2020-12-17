import time
from sympy.ntheory import npartitions

start_time = time.time()

# p(n) = k
n = 5
k = npartitions(n)
while k % 10**6 != 0:
    n += 1
    k = npartitions(n)

print(n)

print("--- %s seconds ---" % (time.time() - start_time))