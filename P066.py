import time
from sympy import symbols
from sympy.solvers.diophantine.diophantine import diop_solve, diophantine, diop_DN

start_time = time.time()
maxx = 0
d = 0
for i in range(2, 1001):
    if round(i**(1/2))**2 != i:
        l = list(diop_DN(i, 1))
        if l[0][0] > maxx:
            maxx = l[0][0]
            d = i

print(d)

print("--- %s seconds ---" % (time.time() - start_time))