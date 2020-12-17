f = open("p067_triangle.txt", "r")
string = f.read()
string = string.replace("\"","")
string = string.split("\n")
string = string[:-1]
for i in range(len(string)):
    string[i] = string[i].split(' ')
    for j in range(len(string[i])):
        string[i][j] = int(string[i][j])


for i in range(len(string) - 2,-1,-1):
    for j in range(len(string[i]) - 1, -1, -1):
        string[i][j] += max(string[i+1][j], string[i+1][j+1])
print(string[0])