# answer will be 6 digits, with three repeating digits
import math
import time
import sys

start_time = time.time()
# sieve
sieve = [1 for i in range(0,1000000)]
for i in range(2, math.ceil(math.sqrt(1000000))):
    for j in range(2, math.ceil(1000000 / i)):
        sieve[i*j] = 0

# perms
perms = [[1,1,1,0,0,0],
         [1,1,0,1,0,0],
         [1,0,1,1,0,0],
         [0,1,1,1,0,0],
         [1,1,0,0,1,0],
         [1,0,1,0,1,0],
         [0,1,1,0,1,0],
         [1,0,0,1,1,0],
         [0,1,0,1,1,0],
         [0,0,1,1,1,0]]


for i in range(100000, 1000000):
    if sieve[i] == 1:
        for x in perms:
            if len(set([str(i)[j] if x[j] == 1  else 'x' for j in range(0,6)])) <= 2 and ('0' in set([str(i)[j] if x[j] == 1  else 'x' for j in range(0,6)]) or '1' in set([str(i)[j] if x[j] == 1  else 'x' for j in range(0,6)]) or '2' in set([str(i)[j] if x[j] == 1  else 'x' for j in range(0,6)]) == {'2', 'x'}): # if permutation is valid to check on i
                famsize = 1
                permutation = x[0] * 100000 + x[1] * 10000 + x[2] * 1000 + x[3] * 100 + x[4] * 10
                for j in range(1, 10):
                    if (i + permutation * j < 1000000):
                        if sieve[i + permutation*j] != 0:
                            famsize += 1
                            if famsize == 8:
                                print("--- %s seconds ---" % (time.time() - start_time))
                                print(i)
                                sys.exit()
