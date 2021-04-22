def sum_numbers(my_list):
    test1 = [int(x) for x in my_list.split() if x.isdigit()]
    return sum(test1)
while True:
    my_list = input('введите числа')
    if (x.isdigit() in my_list) == False:
       z = z + sum_numbers(my_list) 
       break 
    else:
        z = z + sum_numbers(my_list) 
print()