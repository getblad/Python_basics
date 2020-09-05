def my_func(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


a1 = int(input('Введите первую переменную: '))
b1 = int(input('Введите вторую переменную: '))
c1 = int(input('Введите третью переменную: '))

print(my_func(a1, b1, c1))
