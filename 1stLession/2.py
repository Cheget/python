
inputed_seconds = input('Введите время в секундах: ')
print(f'Вы ввели: {inputed_seconds}')

seconds = int(inputed_seconds) % 60
minutes = (int(inputed_seconds) // 60) % 60
hours = int(inputed_seconds) // (60*60)

print(f"Время {hours}:{minutes}:{seconds}")