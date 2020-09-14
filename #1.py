with open('text1.txt', mode='w') as write_dt:
    data = input()
    while data != '':
        write_dt.write(f'{data}\n')
        data = input()


