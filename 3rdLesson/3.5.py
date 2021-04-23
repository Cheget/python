def sum_numbers(my_list, z):
    test1 = [int(x) for x in my_list.split() if x.isdigit()]
    print(z + sum(test1))
    return z + sum(test1)

z = 0
while True:
    my_list = input('введите числа')
    my_list_to_list = list(my_list)
    exit = False
    for i in my_list_to_list:
        if i == 'e':
            exit = True
    if exit == True:
        z = sum_numbers(my_list, z) 
        break
    z = sum_numbers(my_list, z) 
    
