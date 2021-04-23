def int_func(words):
    [x.lower() for x in words]
    return ' '.join([x.capitalize() for x in words])

wordsInput = input('введите слова маленькими буквами для обработки: ')
wordsList = wordsInput.split()
print(int_func(wordsList))
