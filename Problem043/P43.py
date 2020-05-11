from itertools import permutations as perm

def hasproperty(numberstring):
    if int(numberstring[1:4]) % 2 == 0 and int(numberstring[2:5]) % 3 == 0 and int(numberstring[3:6]) % 5 == 0 and int(
            numberstring[4:7]) % 7 == 0 and int(numberstring[5:8]) % 11 == 0 and int(
            numberstring[6:9]) % 13 == 0 and int(numberstring[7:10]) % 17 == 0:
        return True
    else:
        return False

def calc():
    specialnumbers = []
    perms = list(perm('12345678900'[:-1], 10))
    numberstring = ''
    for j in range(len(perms)):
        for k in range(len(perms[j])):
            numberstring += perms[j][k]
        if numberstring[0] != '0' and hasproperty(numberstring):
            specialnumbers.append(int(numberstring))
        numberstring = ''
    return sum(specialnumbers)
print(calc())