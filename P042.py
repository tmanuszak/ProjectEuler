f = open("p042_words.txt", "r")
string = f.read()
string = string.replace("\"","")
string = string.split(",")
scoreArray = []

for i in range(len(string)):  # length of string of names
    score = 0
    for j in range(len(string[i])):  # length of word
        score += ord(string[i][j]) - 64
    scoreArray.append(score)

maxScore = max(scoreArray)
n = 0
trinumbers = []
while n*(n+1)/2 <= maxScore:
    trinumbers.append(int(n*(n+1)/2))
    n += 1

count = 0
for i in range(len(scoreArray)):
    if scoreArray[i] in trinumbers:
        count += 1

print(count)