import math
import time
from sympy import sieve, totient

start_time = time.time()
# F_n = sum([totient(i) for i in range(1,9)]) + 1
# print(math.ceil(F_n / 2) - math.ceil(F_n / 3) - 1)
def farey_sequence(n: int) -> None:
    """Print the n'th Farey sequence. Allow for either ascending or descending."""
    (a, b, c, d) = (1, 3, 4000, 11999)
    while c <= n and c != 1 and d != 2:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        global total
        total += 1
total = 0
farey_sequence(12000)

print(total)

print("--- %s seconds ---" % (time.time() - start_time))