import random

file = open('data.txt')
data = file.read()

data = data.split()

new = random.sample(data, 50)
print(new[0].capitalize(), *new[1:], '\n')

new = random.sample(data, 100)
print(new[0].capitalize(), *new[1:], '\n')

new = random.sample(data, 100)
print(new[0].capitalize(), *new[1:], '\n')

new = random.sample(data, 50)
print(new[0].capitalize(), *new[1:], '\n')
