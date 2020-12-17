from sympy import primefactors
import time

start_time = time.time()

l = [1, 0]

n = 2
found = False
while found == False:
    l.append(sum(sum(primefactors(k)) * l[n - k] for k in range(1, n + 1)) / n)
    if l[-1] >= 5000:
        found = True
    n += 1

print(len(l) - 1)
print("--- %s seconds ---" % (time.time() - start_time))