def int_func(word):
    word = list(word)
    word[0] = word[0].upper()
    return ''.join(word)
def string(str):
    str = str.split()
    str1 = ''
    for i in str:
        str1 += f'{int_func(i)} '
    return str1


word = input('Введите слово: ')
print(int_func(word))
str = input('Введите строку: ')
print(string(str))