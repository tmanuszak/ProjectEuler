from num2words import num2words
string = ""
for i in range(1,1001):
    string += num2words(i, lang="en")
total = 0
for i in range(len(string)):
    if ord(string[i]) != 45 and ord(string[i]) != 32:
        total += 1
print(total)