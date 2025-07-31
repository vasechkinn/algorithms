file = open('data.txt', 'r')
data = file.read()
data = data.split('\n')

file.close()
print(data)