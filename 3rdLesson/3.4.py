def my_func_easy(x, y):
    return x ** y


def my_func_hard(x,y):
    y = abs(y)
    z = x
    print(y)
    while y != 1:
        y = y - 1
        z = z * x
    return 1 / z
userNumber = int(input('Введите целое число для возведения в степень '))
userPow = int(input('Введите отрицательное целое число для возведения в нее '))

print(my_func_hard(userNumber, userPow))
print(my_func_easy(userNumber, userPow))