class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return Cell(sub)
        else:
            print(f'Из клетки {self.get_name()} невозможно вычесть {other.get_name()}', end='')
            return ''

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def __str__(self):
        return str(self.quantity)

    def get_name(self):
        for k, v in globals().items():
            if v is self:
                return k

    def make_order(self, row):
        a = ''
        if row > self.quantity:
            return f'{"*" * self.quantity}'
        n = 0
        for i in range(self.quantity//row + 1):
            if self.quantity - n < row:
                a = ''.join([a, f'{"*" * (self.quantity - n)}\n'])
                return a
            a = ''.join([a, f'{"*" * row}\n'])
            n += row
        return a


x = Cell(3)
y = Cell(11)

print(y - x)
print(x - y)
print(x*y)
print(x+y)
print(x/y)
print(y/x)
print(y.make_order(2))
