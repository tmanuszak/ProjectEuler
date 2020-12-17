def addreverse(number):
    return number + int(str(number)[::-1])


def ispalindrome(num):
    return str(num) == str(num)[::-1]


count = 0
iterations = 0
is_lychrel = True
for i in range(1, 10000):
    num = i
    while iterations < 50 and is_lychrel is True:
        num = addreverse(num)
        if ispalindrome(num):
            is_lychrel = False
        else:
            iterations += 1
    if is_lychrel:
        count += 1
    is_lychrel = True
    iterations = 0
print(count)