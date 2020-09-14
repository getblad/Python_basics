from itertools import cycle


dict = {}
with open('text6.txt', 'r', encoding='UTF-8') as txt:
    for line in txt:
        subject = ''.join(line.split()[:1])[:-1]
        sum = 0
        for a, n in zip(line.split()[1:], cycle([3, 4, 5])):
            if a == '—':
                continue
            sum += int(a[:-n])
        dict[subject] = sum
print(dict)