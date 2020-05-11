def ispandigital(numberstr):
    S = set()
    for i in range(len(numberstr)):
        S.add(numberstr[i])
    if S == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        return True
    else: return False


def run():
    numberstr = ''
    counter = 1
    index = 9876
    while index > 1:
        while len(numberstr) < 9:
            numberstr += str(counter * index)
            counter += 1
        if len(numberstr) == 9 and ispandigital(numberstr):
            return numberstr
        else:
            counter = 1
            index += -1
            numberstr = ''

print(run())