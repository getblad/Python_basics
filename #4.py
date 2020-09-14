numbers = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
with open('text4.txt', 'r', encoding='UTF-8') as txt1:
    with open('text4_1.txt', 'w', encoding='UTF-8') as txt2:
        for line in txt1:
            x = line.split(" — ")
            try:
                txt2.write(f'{numbers[x[0]]} — {x[1]}')
            except KeyError:
                print('В исходном файле обнаружена ошибка соответствия!')
