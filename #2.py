class ZeroDivision(Exception):
    def __init__(self):
        self.txt = 'На ноль делить нелязя!'


a = int(input())
b = int(input())
try:
    if b == 0:
        raise ZeroDivision
except ZeroDivision as err:
    print(err)
else:
    print(a / b)

