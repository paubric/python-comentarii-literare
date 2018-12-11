import random

file = open('data.txt')
data = file.read()

data = data.split()
new = random.sample(data, 100)
print(*new)
