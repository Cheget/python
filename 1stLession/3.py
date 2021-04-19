inputed_value = input('Введите число: ')
print(f'Вы ввели: {inputed_value}')
while inputed_value.isdigit()==False:
    inputed_value = input('Строка должна содержать только цифры. Введите число: ')
    
result = int(inputed_value) + int(inputed_value + inputed_value) + int(inputed_value + inputed_value + inputed_value)

print(f"{inputed_value} + {inputed_value + inputed_value} + {inputed_value + inputed_value + inputed_value} = {result}")
