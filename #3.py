with open('text3.txt', 'r', encoding='UTF-8') as txt:
    average = 0
    count = 0
    for line in txt:
        try:
            salary = int(line.split(' - ')[1])
            if salary < 20000:
                print(line, end='')
            average += salary
            count += 1
        except ValueError:
            print('В файле обнаружена ошибка ввода заработной платы!')
        except IndexError:
            break
    print(f'Средняя заработанная плата {average/count:.2f}')

