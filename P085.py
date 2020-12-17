import math
import time

start_time = time.time()

n = 1
m = 1
dim = (0, 0)
closestarea = 0
closestsols = 1000000000000000
previousrects = 0
while n * (n + 1) * m * (m + 1) / 4 < 2000000:
    while n * (n + 1) * m * (m + 1) / 4 < 2000000:
        previousrects = n * (n + 1) * m * (m + 1) / 4
        m += 1
    if abs(2000000 - previousrects) < abs(2000000 - (n * (n + 1) * m * (m + 1) / 4)): # if the previous was closer
        if abs(2000000 - previousrects) < closestsols: # previous rects is new closest solution
            closestsols = abs(2000000 - previousrects)
            closestarea = n * (m - 1)
            dim = (n, m - 1)
    elif abs(2000000 - previousrects) > abs(2000000 - (n * (n + 1) * m * (m + 1) / 4)): # if the new grid is closer
        if abs(2000000 - (n * (n + 1) * m * (m + 1) / 4)) < closestsols:
            closestsols = abs(2000000 - (n * (n + 1) * m * (m + 1) / 4))
            closestarea = n * m
            dim = (n, m)
    else:
        if abs(2000000 - (n * (n + 1) * m * (m + 1) / 4)) < closestsols:
            closestsols = abs(2000000 - (n * (n + 1) * m * (m + 1) / 4))
            closestarea = n * m
            dim = (n, m)
    n += 1
    m = n

print(closestarea)
print(closestsols)
print(dim)

print("--- %s seconds ---" % (time.time() - start_time))