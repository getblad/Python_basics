def my_func(x, y):
    return x**y
def my_func2(x, y):
    k = 1
    for i in range (abs(y)):
        k *= 1/x
    return k


a = int(input('Введите переменную: '))
b = int(input('Введите степень: '))
print(my_func(a, b), my_func2(a, b))
