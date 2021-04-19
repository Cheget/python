
my_list = []
my_int = 123
my_string = "test_string"
my_float = 5.92929
my_bool = True
my_byte = bytes(my_string, 'utf-8')
my_list.append(my_int)
my_list.append(my_string)
my_list.append(my_float)
my_list.append(my_bool)
my_list.append(my_byte)

for i in my_list:
    print(type(i))

