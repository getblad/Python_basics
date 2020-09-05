def sumnumbers():
    suma = 0
    while True:
        x = input('Введите числа через пробел: ').split()
        for a in x:
            if a.upper() == 'Q':
                return suma
            suma += int(a)
        print(suma)
        if input('Введите q для выхода из программы. Для продолжения работы нажмите Enter - ').upper() == 'Q':
            break
    return suma

print(sumnumbers())
