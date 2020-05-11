f = open("p022_names.txt", "r")
string = f.read()
string = string.replace("\"","")
string = string.split(",")
string = sorted(string)
scoreArray = []

for i in range(len(string)):  # length of string of names
    score = 0
    for j in range(len(string[i])):  # length of word
        score += ord(string[i][j]) - 64
    score *= i + 1
    scoreArray.append(score)

print(sum(scoreArray))