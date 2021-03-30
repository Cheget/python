
empty_list = []

friends = ['Max', 'Leo','Kate']

print(type(friends))

print('Второй друг:', friends[1])
print('Первый друг с конца', friends[-1])


print(friends[1:2])

print(friends[:2])

print(friends[1:])
print(len(friends))

friends.append('George')
friends.append('Dyayda Vana')

print(len(friends))

friends.remove('George')
print(friends)
del friends[3]
print(friends)

