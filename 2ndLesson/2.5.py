my_list = [7, 5, 3, 3, 2]
userInput = int(input('Введите число: '))
if userInput in my_list:
    my_list.append(userInput)
    my_list.sort(reverse=True)
    print(my_list)
else:
    my_list.append(userInput)
    my_list.sort(reverse=True)
    my_list.pop(len(my_list) - 1)
    print(my_list)