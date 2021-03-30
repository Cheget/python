"""
name = 'George'
age = 2
period = 2

print(type(name))
print(name, age)

print(name,age, sep='.')




user_input = int(input('Введите число: '))
user_input += 2
print(user_input)


user_input = int(input('Введите число: '))
while user_input > 10 or user_input < 0: 

    #user_input = int(input('Писло не верное, ведите число > 10 и < 0: '))
print(user_input**2)
"""

user_age = int(input('Введите ваш возраст: '))
user_weight = int(input('Введите ваш вес: '))

if user_age < 30 and (user_weight > 50 or user_weight < 120):
    print('Вы в нормальнои состоянии')

elif (user_age > 30 and user_age < 40) and (user_weight < 50 or user_weight > 120 ):
    print('Чувак займись собой')

elif (user_age >= 40 and user_age < 60) and (user_weight < 50 or user_weight > 120 ):
    print('Иди к врачу')

elif user_age > 60 and (user_weight < 50 or user_weight > 120):
    print('иди на кладбище')
    


