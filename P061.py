import sys
import time
import math
from itertools import permutations

start_time = time.time()
triangle = [i if math.sqrt(8 * i + 1) == math.floor(math.sqrt(8 * i + 1)) else 0 for i in range(0, 10000)]
square = [i if math.sqrt(i) == math.floor(math.sqrt(i)) else 0 for i in range(0, 10000)]
pentagonal = [i if math.sqrt(24 * i + 1) == math.floor(math.sqrt(24 * i + 1)) and math.sqrt(24 * i + 1) % 6 == 5 else 0 for i in range(0, 10000)]
hexagonal = [i if (math.sqrt(8 * i + 1) + 1) / 4 == math.floor((math.sqrt(8 * i + 1) + 1) / 4) else 0 for i in range(0, 10000)]
heptagonal = [i if (math.sqrt(40 * i + 9) + 3) / 10 == math.floor((math.sqrt(40 * i + 9) + 3) / 10) else 0 for i in range(0, 10000)]
octagaonal = [i if (math.sqrt(3 * i + 1) + 1) / 3 == math.floor((math.sqrt(3 * i + 1) + 1) / 3) else 0 for i in range(0, 10000)]

def has_square(num, perm, d, l):
    lis = l.copy()
    firstdigits = (int(str(num)[-2:]) * 100) + 10
    squares = [square[i] for i in range(firstdigits, firstdigits + 90) if square[i] != 0]
    if d == 5 and len(squares) > 0: # we might have found it, check with the triangle number
        for i in range(0, len(squares)):
            if str(squares[i])[-2:] == str(lis[0])[0:2]: # we found it
                lis.append(squares[0])
                print(lis)
                print(" sum is " + str(sum(lis)))
                print("--- %s seconds ---" % (time.time() - start_time))
                sys.exit()
    elif len(squares) > 0:
        for i in range(0, len(squares)): # find the next depth
            lis.append(squares[i])
            ind = perm.index(d + 1)
            if ind == 1:  # has pent
                has_pentagonal(squares[i], perm, d + 1, lis)
            elif ind == 2:  # has hex
                has_hexagonal(squares[i], perm, d + 1, lis)
            elif ind == 3:  # has hep
                has_heptagonal(squares[i], perm, d + 1, lis)
            elif ind == 4:  # has oct
                has_octagonal(squares[i], perm, d + 1, lis)
    else:
        return 0
    return 0

def has_pentagonal(num, perm, d, l):
    lis = l.copy()
    firstdigits = (int(str(num)[-2:]) * 100) + 10
    pents = [pentagonal[i] for i in range(firstdigits, firstdigits + 90) if pentagonal[i] != 0]
    if d == 5 and len(pents) > 0: # we might have found it, check with the triangle number
        for i in range(0, len(pents)):
            if str(pents[i])[-2:] == str(lis[0])[0:2]: # we found it
                lis.append(pents[0])
                print(lis)
                print(" sum is " + str(sum(lis)))
                print("--- %s seconds ---" % (time.time() - start_time))
                sys.exit()
    elif len(pents) > 0:
        for i in range(0, len(pents)): # find the next depth
            lis.append(pents[i])
            ind = perm.index(d + 1)
            if ind == 0:  # has pent
                has_square(pents[i], perm, d + 1, lis)
            elif ind == 2:  # has hex
                has_hexagonal(pents[i], perm, d + 1, lis)
            elif ind == 3:  # has hep
                has_heptagonal(pents[i], perm, d + 1, lis)
            elif ind == 4:  # has oct
                has_octagonal(pents[i], perm, d + 1, lis)
    else:
        return 0
    return 0

def has_hexagonal(num, perm, d, l):
    lis = l.copy()
    firstdigits = (int(str(num)[-2:]) * 100) + 10
    hexs = [hexagonal[i] for i in range(firstdigits, firstdigits + 90) if hexagonal[i] != 0]
    if d == 5 and len(hexs) > 0: # we might have found it, check with the triangle number
        for i in range(0, len(hexs)):
            if str(hexs[i])[-2:] == str(lis[0])[0:2]: # we found it
                lis.append(hexs[0])
                print(lis)
                print(" sum is " + str(sum(lis)))
                print("--- %s seconds ---" % (time.time() - start_time))
                sys.exit()
    elif len(hexs) > 0:
        for i in range(0, len(hexs)): # find the next depth
            lis.append(hexs[i])
            ind = perm.index(d + 1)
            if ind == 0:  # has pent
                has_square(hexs[i], perm, d + 1, lis)
            elif ind == 1:  # has hex
                has_pentagonal(hexs[i], perm, d + 1, lis)
            elif ind == 3:  # has hep
                has_heptagonal(hexs[i], perm, d + 1, lis)
            elif ind == 4:  # has oct
                has_octagonal(hexs[i], perm, d + 1, lis)
    else:
        return 0
    return 0

def has_heptagonal(num, perm, d, l):
    lis = l.copy()
    firstdigits = (int(str(num)[-2:]) * 100) + 10
    hepts = [heptagonal[i] for i in range(firstdigits, firstdigits + 90) if heptagonal[i] != 0]
    if d == 5 and len(hepts) > 0: # we might have found it, check with the triangle number
        for i in range(0, len(hepts)):
            if str(hepts[i])[-2:] == str(lis[0])[0:2]: # we found it
                lis.append(hepts[0])
                print(lis)
                print(" sum is " + str(sum(lis)))
                print("--- %s seconds ---" % (time.time() - start_time))
                sys.exit()
    elif len(hepts) > 0:
        for i in range(0, len(hepts)): # find the next depth
            lis.append(hepts[i])
            ind = perm.index(d + 1)
            if ind == 0:  # has pent
                has_square(hepts[i], perm, d + 1, lis)
            elif ind == 1:  # has hex
                has_pentagonal(hepts[i], perm, d + 1, lis)
            elif ind == 2:  # has hep
                has_hexagonal(hepts[i], perm, d + 1, lis)
            elif ind == 4:  # has oct
                has_octagonal(hepts[i], perm, d + 1, lis)
    else:
        return 0
    return 0

def has_octagonal(num, perm, d, l):
    lis = l.copy()
    firstdigits = (int(str(num)[-2:]) * 100) + 10
    octs = [octagaonal[i] for i in range(firstdigits, firstdigits + 90) if octagaonal[i] != 0]
    if d == 5 and len(octs) > 0: # we might have found it, check with the triangle number
        for i in range(0, len(octs)):
            if str(octs[i])[-2:] == str(lis[0])[0:2]: # we found it
                lis.append(octs[0])
                print(lis)
                print(" sum is " + str(sum(lis)))
                print("--- %s seconds ---" % (time.time() - start_time))
                sys.exit()
    elif len(octs) > 0:
        for i in range(0, len(octs)): # find the next depth
            lis.append(octs[i])
            ind = perm.index(d + 1)
            if ind == 0:  # has pent
                has_square(octs[i], perm, d + 1, lis)
            elif ind == 1:  # has hex
                has_pentagonal(octs[i], perm, d + 1, lis)
            elif ind == 2:  # has hep
                has_hexagonal(octs[i], perm, d + 1, lis)
            elif ind == 3:  # has oct
                has_heptagonal(octs[i], perm, d + 1, lis)
    else:
        return 0
    return 0

perms = list(permutations([1,2,3,4,5], 5))
for i in range(1010, 10000):
    if triangle[i] == 0 or i % 100 < 10:
        continue
    else:
        for j in range(0, len(perms)):
            l = [i]
            index = perms[j].index(1)
            if index == 0:  # has square
                has_square(i, perms[j], 1, l)
            elif index == 1: # has pent
                has_pentagonal(i, perms[j], 1, l)
            elif index == 2: # has hex
                has_hexagonal(i, perms[j], 1, l)
            elif index == 3: # has hep
                has_heptagonal(i, perms[j], 1, l)
            elif index == 4: # has oct
                has_octagonal(i, perms[j], 1, l)

