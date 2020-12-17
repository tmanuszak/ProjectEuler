import math
import time
import matplotlib.pyplot as plt

start_time = time.time()


def facsum(n):
    return sum([math.factorial(int(str(n)[i])) for i in range(0, len(str(n)))])


nums = [0 for i in range(1000000)]
d = {}
for i in range(0, len(nums)):
    if nums[i] == 0:
        chain = [i]
        fac = facsum(i)
        found = False  # if we find fac in nums or the dict, turn to true and dont add it to the chain
        while found == False and fac not in chain:
            if fac < len(nums):  # check nums
                if nums[fac] == 0:  # not in nums so add it to the chain
                    chain.append(fac)
                    fac = facsum(fac)
                else:  # we found it in nums
                    found = True
            else:
                if fac not in d:  # fac is not in the dictionary
                    chain.append(fac)
                    fac = facsum(fac)
                else:  # found fac in the dictionary
                    found = True

        if fac in chain:  # we have NOT seen ANY of the chain #'s before
            fac_index = chain.index(fac)
            before_loop = chain[0:fac_index]
            loop = chain[fac_index:]

            for j in range(0, len(before_loop)):
                if before_loop[j] < len(nums):
                    nums[before_loop[j]] = len(chain) - j
                else:
                    d[before_loop[j]] = len(chain) - j

            for j in range(0, len(loop)):
                if loop[j] < len(nums):
                    nums[loop[j]] = len(loop)
                else:
                    d[loop[j]] = len(loop)

        else:  # Broke while loop because we know length of frac
            # get fac length
            if fac < len(nums):  # we found it in nums
                fac_length = nums[fac]
            else:
                fac_length = d[fac]

            # input lengths
            for j in range(1, len(chain) + 1):  # going to fill backwards
                if chain[-j] < len(nums):
                    nums[chain[-j]] = fac_length + j
                else:
                    d[chain[-j]] = fac_length + j

data = []
for i in range(1, 61):
    data.append((i,len([1 for j in range(0, len(nums)) if nums[j] == i])))

x_val = [x[0] for x in data]
y_val = [x[1] for x in data]

plt.plot(x_val,y_val)
plt.plot(x_val,y_val,'or')
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))
