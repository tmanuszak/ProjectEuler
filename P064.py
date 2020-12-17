import time
from sympy.ntheory.continued_fraction import continued_fraction_periodic

start_time = time.time()

oddcount = 0
for i in range(2, 10001):
    if round(i**(1/2))**2 != i:
        c = continued_fraction_periodic(0, 1, i)
        if len(c[1]) % 2 == 1:
            oddcount += 1

print(oddcount)

# THIS IS A MUCH FASTER ALGO FOUND ON THE FORUM
# def findPeriod(n):
#     d = int(n ** 0.5)
#     if n == d ** 2: return [d, []]
#
#     c = n - d ** 2
#     a = int((2 * d) / (n - (d ** 2)))
#     b = a * c - d
#
#     b0 = b
#     c0 = c
#     a0 = [a]
#
#     while True:
#         c = int((n - (b ** 2)) / c)
#         a = int((d + b) / c)
#         b = a * c - b
#
#         if (b, c) == (b0, c0):
#             return [d, a0]
#         else:
#             a0.append(a)
#
#
# s = 0
# for i in range(1, 10001):
#     p = findPeriod(i)
#     if len(p[1]) % 2 == 1:
#         s += 1
#
# print(s)

print("--- %s seconds ---" % (time.time() - start_time))