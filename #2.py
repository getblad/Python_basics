with open('text2.txt', 'r') as txt:
    string = 1
    for line in txt:
        print(f'количество слов в строке {string} - {len(line.split())}')
        string += 1
