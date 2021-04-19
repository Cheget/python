my_list = []
my_list.append(input('введите данные в список, done - завершение заполнения списка '))
i = 0
while my_list[i]!='done':
    my_list.append(input("введите данные в список, done - завершение заполнения списка "))
    i = i+1
print(my_list)
if (len(my_list) % 2) != 0:
    my_list[:-1:2], my_list[1:-1:2] = my_list[1:-1:2], my_list[:-1:2]
else: 
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]   

print(my_list)

