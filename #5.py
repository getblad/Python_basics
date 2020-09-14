from random import randint


with open('text5.txt', 'w', encoding='UTF-8') as txt:
    for i in range(5):
        txt.write(f'{str(randint(1, 100))} ')
with open('text5.txt', 'r', encoding='UTF-8') as txt:
    print(sum(map(int, txt.readline().split())))
