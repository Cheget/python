def test_function(x, y):
    if y == 0:
        print('Делить на ноль нельзя, программа завершается')
    else:
        return x / y
input_x = int(input("Введите x: "))
input_y = int(input("Введите y: "))
print(test_function(input_x, input_y))   