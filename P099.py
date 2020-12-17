import math
import time

a_file = open("p099_base_exp.txt", "r")

list_of_lists = [(line.strip()).split(",") for line in a_file]

a_file.close()

for i in range(len(list_of_lists)):
    list_of_lists[i].append(i + 1)

start_time = time.time()

while len(list_of_lists) > 1:
    largest = int(list_of_lists[0][1]) * math.log2(int(list_of_lists[0][0]))
    for i in range(1,len(list_of_lists)):
        if largest > (int(list_of_lists[1][1]) * math.log2(int(list_of_lists[1][0]))):
            list_of_lists.pop(1)
        else:
            list_of_lists.pop(0)
            break
print("--- %s seconds ---" % (time.time() - start_time))
print(list_of_lists)