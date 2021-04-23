def my_func(a, b, c):
    l = [a, b, c ]
    return max(l[1:2]) + max(l[2:3])
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print(f'Сумма наибольших двух равна {my_func(a, b, c)}')