apple = {'color': 'red', 'taste': 'sweat'}
pasta = {'color': 'yellow?', 'taste': '파스타 맛'}

print(apple['color'])
print(pasta['color'])
print(apple['taste'])
print(pasta['taste'])


apple['ETA'] = 1
pasta['ETA'] = 48

def addoneeta(food):
    food['ETA'] += 1

addoneeta(apple)
addoneeta(pasta)

print(apple['ETA'])
print(pasta['ETA'])

print(apple.items())

for key, value in apple.items():
    print('key:{}, value:{}'.format(key,value))

q_food = input('어떤 음식에 대해서 알려드릴까요?')

for key, value in q_food.items():
    print('key:{}, value:{}'.format(key,value))



