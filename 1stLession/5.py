profit_value = input('Введите размер выручки: ')
while profit_value.isdigit()==False:
    profit_value = input(f'Строка должна содержать только цифры, а вы ввели {profit_value} Введите размер выручки: ')

loss_value = input('Введите размер издержек: ')
while loss_value.isdigit()==False:
    loss_value = input(f'Строка должна содержать только цифры, а вы ввели {loss_value} Введите размер издержек: ')

if int(profit_value) <= int(loss_value):
    print('Вы работаете в убыток')
elif int(profit_value) >= int(loss_value):
    x = int(profit_value) - int(loss_value)
    print(f'Вы работаете с прибылью. Размер прибыли:{x}')
    emploee = input('Введите количество сотрдуников для рассчета прибыли на одного сотрудника: ')
    y = x / int(emploee)
    print(f'Прибыль на одного сотрудника {y}')

