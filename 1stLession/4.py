inputed_value = input('Введите число: ')
print(f'Вы ввели: {inputed_value}')
while inputed_value.isdigit()==False:
    inputed_value = input('Строка должна содержать только цифры. Введите число: ')
    
numbers = list(inputed_value)
i = 0 
result = numbers[i]
while i < len(numbers):
    if numbers[i] > result:
        result = numbers[i]
    i += 1
print(f"Самое больше число в введенной вами последовательности: {result}")