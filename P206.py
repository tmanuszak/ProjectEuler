import math

for i in range(1058921250, math.ceil(math.sqrt(1929394959697989990)), 30):
    if [int(str(i**2)[j]) for j in range(len(str(i**2))) if j % 2 == 0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        print(i)
        break
