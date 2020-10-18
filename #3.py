class OnlyNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


x = input()
a = []
while x != 'stop':
    try:
        if not x.isnumeric():
            raise OnlyNumber('Необходимо ввести число!')
        else:
            a.append(int(x))
    except OnlyNumber as err:
        print(err)
    x = input()
print(a)


