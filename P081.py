import time
import re

start_time = time.time()

with open('p081_matrix.txt', 'r') as file:
    data = file.read()
    data = re.split(',|\n', data)
    data = data[:-1]
    file.close()

d = []
for i in range(0, 80):
    d.append([int(data[j]) for j in range((i * 80), ((i + 1) * 80))])

for i in range(78, -1, -1):
    d[79][i] += d[79][i + 1] # get bottom row
    d[i][79] += d[i + 1][79]

for i in range(78, -1, -1):
    for j in range(78, -1, -1):
        d[i][j] += min(d[i + 1][j], d[i][j + 1])

print("--- %s seconds ---" % (time.time() - start_time))