import math


def isPentagonal(number):
    if math.sqrt(24 * number + 1) % 6 == 5:
        return True
    else:
        return False


def isTriangular(number):
    if math.sqrt(8 * number + 1) % 2 == 1:
        return True
    else:
        return False


answer = 0
flag = False
index = 144
while flag is False:
    if isPentagonal(2 * index ** 2 - index) and isTriangular(2 * index ** 2 - index):
        flag = True
        print(2 * index ** 2 - index)
    else:
        index += 1
