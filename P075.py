import math
import time
import numpy as np

start_time = time.time()

limit = 1500000

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)


l = list(gen_prim_pyth_trips(748229)) # list of unique pyth triples
l = [l[i] for i in range(0, len(l)) if sum(l[i]) <= limit] # list of unique pyth triples with sum less than limit
length = [0 for i in range(0, limit + 1)]
for i in range(0, len(l)):
    s = sum(l[i])
    for i in range(1, math.floor(len(length) / s) + 1):
        length[s * i] += 1
print(len([1 for i in range(0, len(length)) if length[i] == 1]))

print("--- %s seconds ---" % (time.time() - start_time))