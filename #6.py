class OnlyNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    items = {'Printer': [0], 'Scanner': [0], 'Xerox': [0]}

    @staticmethod
    def count(type):
        print(Stock.items[type][0])


class Equipment(Stock):
    pass


class Printer(Equipment):
    def __init__(self, name, price, quantity=1):
        self.price = price
        self.name = name
        self.quantity = quantity
        self.location = None

    def stock(self):
        try:
            if not isinstance(self.quantity, int):
                raise OnlyNumber('Необходимо ввести число!')
            else:
                Stock.items['Printer'][0] += self.quantity
                for i in range(self.quantity):
                    Stock.items['Printer'].append({self.name: self.price})
                self.location = 'Stock'
        except OnlyNumber as err:
            print(err)
            self.quantity = int(input('Введите количество: '))
            self.stock()

    def move(self, where):
        self.location = where
        for i in range(self.quantity):
            Stock.items['Printer'].remove({self.name: self.price})
        Stock.items['Printer'][0] -= self.quantity


class Scanner(Equipment):
    def __init__(self, name, price, quantity=1):
        self.price = price
        self.name = name
        self.quantity = quantity
        self.location = None

    def stock(self):
        try:
            if not isinstance(self.quantity, int):
                raise OnlyNumber('Необходимо ввести число!')
            else:
                Stock.items['Scanner'][0] += self.quantity
                for i in range(self.quantity):
                    Stock.items['Scanner'].append({self.name: self.price})
                self.location = 'Stock'
        except OnlyNumber as err:
            print(err)
            self.quantity = int(input('Введите количество: '))
            self.stock()

    def move(self, where):
        self.location = where
        for i in range(self.quantity):
            Stock.items['Scanner'].remove({self.name: self.price})
        Stock.items['Scanner'][0] -= self.quantity


class Xerox(Equipment):
    counter = 0

    def __init__(self, name, price, quantity=1):
        self.price = price
        self.name = name
        self.location = None
        self.quantity = quantity

    def stock(self):
        try:
            if not isinstance(self.quantity, int):
                raise OnlyNumber('Необходимо ввести число!')
            else:
                Stock.items['Xerox'][0] += self.quantity
                for i in range(self.quantity):
                    Stock.items['Xerox'].append({self.name: self.price})
                self.location = 'Stock'
        except OnlyNumber as err:
            print(err)
            self.quantity = int(input('Введите количество: '))
            self.stock()

    def move(self, where):
        self.location = where
        for i in range(self.quantity):
            Stock.items['Xerox'].remove({self.name: self.price})
        Stock.items['Xerox'][0] -= self.quantity


Epson = Printer('Epson', 23142, '1')
Epson.stock()
Stock.count('Printer')
print(Stock.items)
Epson.move('12')
print(Stock.items)