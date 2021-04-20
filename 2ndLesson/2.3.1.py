userInput = int(input('Введите число от 1 до 12'))
while (userInput in range(1,13)) != True:
    userInput = int(input(f'Строка должна содержать только цифры от 1 до 12, а вы ввели {userInput} Введите число от 1 до 12: '))
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]
if userInput in spring:
    print('весна')
elif userInput in summer:
    print('лето')
elif userInput in autumn:
    print('осень')
elif userInput in winter:
    print('зима')