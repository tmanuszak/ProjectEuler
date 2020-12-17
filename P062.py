import sys
import time

def makelargestperm(n):
    s = [str(n)[i] for i in range(0, len(str(n)))]
    s.sort(reverse=True)
    return int(''.join(map(str,s)))

start_time = time.time()
number = 344
d = {}
while True:
    k = makelargestperm(number**3)
    if k in d.keys():
        d[k].append(number**3)
        if len(d[k]) == 5:
            print(d[k])
            print("--- %s seconds ---" % (time.time() - start_time))
            sys.exit()
    else:
        d[k] = [number**3]
    number += 1
