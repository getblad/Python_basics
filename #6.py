from itertools import cycle, count


n = 3
list = [1, 2, 3, 'abd', 4]


for a in count(n):
    if a == n+10:
        break
    print(a)

c = 0

for a in cycle(list):
    print(a)
    c+=1
    if c == 10:
        break