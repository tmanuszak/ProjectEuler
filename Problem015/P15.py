from sympy import zeros

M = zeros(21, 21)
M[0, 0] = 1

for i in range(1, 21):  # top left of matrix calculate
    for j in range(i, -1, -1):  # row index
        if i - j > 0:  # if there is an element to the left
            M[j, i - j] += M[j, i - j - 1]
        if j > 0:  # if the is an element above the current position
            M[j, i - j] += M[j - 1, i - j]

for i in range(1, 21):  # bottom right of matrix calculate
    for j in range(20, i - 1, -1):
        row = j
        column = 20 + i - j
        M[j, 20 + i - j] += M[j, 19 + i - j]  # add element to the left
        M[j, 20 + i - j] += M[j - 1, 20 + i - j]  # add element above
print(M[20, 20])
