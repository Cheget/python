inputString = input('Введите строку разделенную пробелами: ')
splitedString = inputString.split()
print(splitedString)
for i in range(len(splitedString)):
    if len(splitedString[i]) < 10:
        print(f"{i} {splitedString[i]}" )
    else: 
        tempString = splitedString[i]
        print(f"{i} {tempString[::10]}" )
    