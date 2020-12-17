with open('p079_keylog.txt', 'r') as file:
    data = file.read().split('')
    file.close()
    dataset = set(data)
    dataset.remove('')

print(data)