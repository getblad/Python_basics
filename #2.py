def user(name, surname, year, city, e_mail, phonenumber):
    return f'Пользователь {name} {surname} {year} года рождения, проживает в городе {city}. ' \
           f'Телефон для связи {phonenumber}, e-mail: {e_mail}'
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город: ')
e_mail = input('Введите e-mail: ')
phonenumber = input('Введите телефон: ')
print(user(name=name, surname=surname, year=year, city=city, e_mail=e_mail, phonenumber=phonenumber))