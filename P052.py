def ispermutation(number1, number2):
    S1 = sorted([number1[i] for i in range(len(number1))])
    S2 = sorted([number2[i] for i in range(len(number2))])
    if S1 == S2:
        return True
    else:
        return False

flag = False
while flag is False:
    indexi = 10
    while flag is False:
        indexj = 0
        while indexj < ((indexi * 10) / 6) - indexi:
            if ispermutation(str(indexi + indexj), str((indexi + indexj) * 2)) is False:  # Check 2x
                indexj += 1
            elif ispermutation(str(indexi + indexj), str((indexi + indexj) * 3)) is False:  # Check 3x
                indexj += 1
            elif ispermutation(str(indexi + indexj), str((indexi + indexj) * 4)) is False:  # Check 4x
                indexj += 1
            elif ispermutation(str(indexi + indexj), str((indexi + indexj) * 5)) is False:  # Check 5x
                indexj += 1
            elif ispermutation(str(indexi + indexj), str((indexi + indexj) * 6)) is False:  # Check 6x
                indexj += 1
            else:
                flag = True
                print(indexi + indexj)
                break
        indexi = indexi * 10