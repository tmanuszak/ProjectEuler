import time

# royal flush
def rfcheck(h1, h2):
    if (set(h1[0]) == {'T', 'J', 'Q', 'K', 'A'}):
        if (len(set(h1[1])) == 1):
            return 1
    elif (set(h2[0]) == {'T', 'J', 'Q', 'K', 'A'}):
        if (len(set(h2[1])) == 1):
            return 2
    return 0


# straight flush
def sfcheck(h1, h2):
    if len(set(h1[1])) == 1 and len(set(h2[1])) == 1:
        return scheck(h1, h2)
    elif (len(set(h1[1])) == 1):  # if same suit
        if scheck(h1, h2) == 1:
            return 1
    elif (len(set(h2[1])) == 1):  # if same suit
        if scheck(h1, h2) == 2:
            return 2

    return 0


# 4 kind
def fourcheck(h1, h2):
    h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
    h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
    h1[0].sort()
    h2[0].sort()
    win1 = 0
    win2 = 0
    h1val = -1
    h1k = -1
    h2val = -1
    h2k = -1

    if (h1[0].count(h1[0][0])) == 4:
        h1val = h1[0][0]
        h1k = h1[0][-1]
        win1 = 1
    elif (h1[0].count(h1[0][-1])) == 4:
        h1val = h1[0][-1]
        h1k = h1[0][0]
        win1 = 1
    if (h2[0].count(h2[0][0])) == 4:
        h2val = h2[0][0]
        h2k = h2[0][-1]
        win2 = 1
    elif (h2[0].count(h2[0][-1])) == 4:
        h2val = h2[0][-1]
        h2k = h2[0][0]
        win2 = 1
    if win1 == win2 and win1 != 0:  # tie, but impossible to check kicker
        if h1val == h2val:
            h1[0] = [h1k]
            h2[0] = [h2k]
            return hcheck(h1, h2)
        elif h1val > h2val:
            return 1
        else:
            return 2
    elif win1 == 1:
        return 1
    elif win2 == 1:
        return 2
    return 0


# full house
def fhcheck(h1, h2):
    h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
    h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
    h1[0].sort()
    h2[0].sort()
    win1 = -1
    hi1 = -1
    lo1 = -1
    win2 = -1
    hi2 = -1
    lo2 = -1

    if (h1[0].count(h1[0][0])) == 3 and (h1[0].count(h1[0][-1])) == 2:
        win1 = 1
        hi1 = h1[0][0]
        lo1 = h1[0][-1]
    elif (h1[0].count(h1[0][0])) == 2 and (h1[0].count(h1[0][-1])) == 3:
        win1 = 1
        hi1 = h1[0][-1]
        lo1 = h1[0][0]
    if (h2[0].count(h2[0][0])) == 3 and (h2[0].count(h2[0][-1])) == 2:
        win2 = 1
        hi2 = h2[0][0]
        lo2 = h2[0][-1]
    elif (h2[0].count(h2[0][0])) == 2 and (h2[0].count(h2[0][-1])) == 3:
        win2 = 1
        hi2 = h2[0][-1]
        lo2 = h2[0][0]

    if win1 == win2 and win1 != -1:  # tie
        if hi1 == hi2:
            if lo1 > lo2:
                return 1
            elif lo2 > lo1:
                return 2
            else:
                print("Shouldnt be here full house")
                return 0
        elif hi1 > hi2:
            return 1
        else:
            return 2
    elif win1 == 1:
        return 1
    elif win2 == 1:
        return 2
    return 0


# flush
def fcheck(h1, h2):
    if len(set(h1[1])) == 1 and len(set(h2[1])) == 1: #tie
        h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
        h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
        return hcheck(h1, h2)
    elif len(set(h1[1])) == 1:
        return 1
    elif len(set(h2[1])) == 1:
        return 2
    return 0


# straight
def scheck(h1, h2):
    h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
    h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
    h1[0].sort()
    h2[0].sort()

    if h1[0][-1] - h1[0][0] == 4 and h2[0][-1] - h2[0][0] == 4 and len(set(h1[0])) == 5 and len(set(h2[0])) == 5: #tie
        if h1[0][-1] > h2[0][-1]:
            return 1
        elif h2[0][-1] > h1[0][-1]:
            return 2
        else:
            print("Check this straight out XXXXXXXXXXXXXXXXXXXXXXXXXXX")
    if h1[0][-1] - h1[0][0] == 4 and len(set(h1[0])) == 5:
        return 1
    if h2[0][-1] - h2[0][0] == 4 and len(set(h2[0])) == 5:
        return 2

    return 0


# 3 kind
def threecheck(h1, h2):
    h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
    h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
    h1val = -1
    h2val = -1
    for i in range (0, 5):
        if h1[0].count(h1[0][i]) == 3:
            h1val = h1[0][i]
        if h2[0].count(h2[0][i]) == 3:
            h2val = h2[0][i]
    if h1val == h2val and h1val != -1: # three pairs tie
        set1 = set(h1[0])
        set1.discard(h1val)
        set2 = set(h2[0])
        set2.discard(h2val)
        h1[0] = list(set1)
        h2[0] = list(set2)
        return hcheck(h1, h2)
    elif h1val > h2val:
        return 1
    elif h2val > h1val:
        return 2
    return 0


# 2 pair
def tpcheck(h1, h2):
    h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
    h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
    h1hp = -1 # h1 high pair
    h1lp = -1 # h1 lo pair
    h1k = -1 # h1 kicker
    h2hp = -1
    h2lp = -1
    h2k = -1
    h12p = 0
    h22p = 0
    for i in range(0, 5):
        if h1[0].count(h1[0][i]) == 2 and h1hp == -1:
            h1hp = h1[0][i]
            h12p += 1 # h1 has 1 pair
        elif h1[0].count(h1[0][i]) == 2 and h1[0][i] != h1hp and h1[0][i] != h1lp:
            h1lp = h1[0][i]
            h12p += 1 # h1 has 2 pair
        elif h1[0].count(h1[0][i]) == 1:
            h1k = h1[0][i]
        if h2[0].count(h2[0][i]) == 2 and h2hp == -1:
            h2hp = h2[0][i]
            h22p += 1
        elif h2[0].count(h2[0][i]) == 2 and h2[0][i] != h2hp and h2[0][i] != h2lp:
            h2lp = h2[0][i]
            h22p +=1
        elif h2[0].count(h2[0][i]) == 1:
            h2k = h2[0][i]
    if h1lp > h1hp:
        temp = h1lp
        h1lp = h1hp
        h1hp = temp
    if h2lp > h2hp:
        temp = h2lp
        h2lp = h2hp
        h2hp = temp
    if h12p == 2 and h22p == 2: # tie
        if h1hp == h2hp and h1lp == h2lp: # pairs tie
            h1[0] = [h1k]
            h2[0] = [h2k]
            return hcheck(h1, h2)
        elif h1hp == h2hp:
            if h1lp > h2lp:
                return 1
            else:
                return 2
        elif h1hp > h2hp:
            return 1
        else:
            return 2
    elif h12p == 2:
        return 1
    elif h22p == 2:
        return 2

    return 0


# 1 pair
def opcheck(h1, h2):
    h1[0] = [cardval.index(h1[0][i]) for i in range(0, 5)]
    h2[0] = [cardval.index(h2[0][i]) for i in range(0, 5)]
    h1pairval = -1
    h2pairval = -1

    for i in range(0,5):
        if h1[0].count(h1[0][i]) == 2:
            h1pairval = h1[0][i]
        if h2[0].count(h2[0][i]) == 2:
            h2pairval = h2[0][i]
    if h1pairval == h2pairval and h1pairval != -1: # tie
        set1 = set(h1[0])
        set1.discard(h1pairval)
        set2 = set(h2[0])
        set2.discard(h2pairval)
        h1[0] = list(set1)
        h2[0] = list(set2)
        return hcheck(h1, h2)
    elif h1pairval > h2pairval:
        return 1
    elif h2pairval > h1pairval:
        return 2
    return 0


# high card, parameters must be card valued
def hcheck(h1, h2):
    h1[0].sort()
    h2[0].sort()
    if len(h1[0]) > 0:
        if h1[0][-1] == h2[0][-1]:
            h1[0] = h1[0][0:-1]
            h2[0] = h2[0][0:-1]
            return hcheck(h1, h2)
        elif h1[0][-1] > h2[0][-1]:
            return 1
        elif h2[0][-1] > h1[0][-1]:
            return 2
    return 0


def sep(h):
    arr = []
    arr.append([h[i][0] for i in range(0, 5)])
    arr.append([h[i][1] for i in range(0, 5)])
    return arr

start_time = time.time()
cardval = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
p1wincount = 0
p2wincount = 0

with open('p054_poker.txt', 'r') as file:
    data = file.read().split('\n')
    file.close()

p1 = []
p2 = []
for i in range(len(data)):
    p1.append(data[i].split(' ')[:5])
    p2.append(data[i].split(' ')[5:])

# print(p1)
# hand1 = ['3C', '3C', '3C', '9C', '9C']
# hand2 = ['2C', '2C', '8C', '8C', '8C']
# # hand1 = sep(hand1)
# # hand2 = sep(hand2)
# # hand1[0] = [cardval.index(hand1[0][i]) for i in range(0, 5)]
# # hand2[0] = [cardval.index(hand2[0][i]) for i in range(0, 5)]
# print(fhcheck(sep(hand1), sep(hand2)))
for game in range(0, 1000): # 1000 games
    # this is for hcheck ###########
    hand1 = sep(p1[game])
    hand2 = sep(p2[game])
    hand1[0] = [cardval.index(hand1[0][i]) for i in range(0, 5)]
    hand2[0] = [cardval.index(hand2[0][i]) for i in range(0, 5)]
    ######################
    if (p1wincount + p2wincount != game):
        print("Something went off. It is game # " + str(game))
    if rfcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif rfcheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif sfcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif sfcheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif fourcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif fourcheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif fhcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif fhcheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif fcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif fcheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif scheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif scheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif threecheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif threecheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif tpcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif tpcheck(sep(p1[game]), sep(p2[game])) == 2: 
        p2wincount += 1
        continue
    elif opcheck(sep(p1[game]), sep(p2[game])) == 1:
        p1wincount += 1
        continue
    elif opcheck(sep(p1[game]), sep(p2[game])) == 2:
        p2wincount += 1
        continue
    elif hcheck(hand1, hand2) == 1:
        p1wincount += 1
        continue
    elif hcheck(hand1, hand2) == 2:
        p2wincount += 1
        continue
    print("XXXXXXXXXXXXXXXXX SHOULD NOT BE PRINTING  XXXXXXXXXXXXXXXXXXXXXXXXX Game # " + str(game))

print(p1wincount)
print("--- %s seconds ---" % (time.time() - start_time))