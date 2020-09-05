def div(a, b):
    return a/b
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
try:
    print(div(a, b))
except ZeroDivisionError:
    print('Нельзя делить на ноль!')