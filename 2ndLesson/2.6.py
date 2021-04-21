
items_list = []
item_tuple = ()
item_analitic = {'название': [], 'цена' : [], 'количество': [], 'ед': []}
i = 0
yes = {'yes','y', ''}
no = {'no','n'}
while True:
    item_name = input('Введите название товара: ')
    item_price = input('Введите цену товара: ')
    while  item_price.isdigit() != True:
        item_price = input(f'Строка должна содержать только цифры, а вы ввели {item_price}\n Введите цену: ')
    int(item_price)

    item_quantity = input('Введите количество товара на складе: ')
    while  item_quantity.isdigit() != True:
        item_quantity = input(f'Строка должна содержать только цифры, а вы ввели {item_quantity}\n Введите цену: ')
    int(item_quantity)
    i += 1
    items_list.append(item_tuple + (i, dict(название=item_name, цена=item_price, количество=item_quantity, ед="шт.")))
    breakTrue = input('Добавить новый товар? Y/N')
    if breakTrue in no:
        break
for item in items_list:
    item_analitic['название'].append(item[1]['название']) 
    item_analitic['цена'].append(item[1]['цена']) 
    item_analitic['количество'].append(item[1]['количество']) 
    print(item[1]['ед'])
    print(item_analitic['ед'])
    if item[1]['ед'] in item_analitic['ед'] :
        print("такая еденица измерения уже есть") 
    else:
        item_analitic['ед'].append(item[1]['ед'])  
print(item_analitic)


        


    






