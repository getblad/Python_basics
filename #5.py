class Stock:
    items = {'Printer': [0], 'Scanner': [0], 'Xerox': [0]}

    @staticmethod
    def count(type):
        print(Stock.items[type][0])


class Equipment(Stock):
    all_equipment = 0


class Printer(Equipment):
    counter = 0

    def __init__(self, name, price):
        Equipment.all_equipment += 1
        Printer.counter += 1
        self.price = price
        self.name = name
        self.location = None

    def stock(self):
        Stock.items['Printer'].append({self.name: self.price})
        Stock.items['Printer'][0] += 1
        self.location = 'Stock'

    def move(self, where):
        self.location = where
        Stock.items['Printer'].remove({self.name: self.price})
        Stock.items['Printer'][0] -= 1


class Scanner(Equipment):
    counter = 0

    def __init__(self, name, price):
        Equipment.all_equipment += 1
        Scanner.counter += 1
        self.price = price
        self.name = name
        self.location = None

    def stock(self):
        Stock.items['Scanner'].append({self.name: self.price})
        Stock.items['Scanner'][0] += 1
        self.location = 'Stock'

    def move(self, where):
        self.location = where
        Stock.items['Scanner'].remove({self.name: self.price})
        Stock.items['Scanner'][0] -= 1


class Xerox(Equipment):
    counter = 0

    def __init__(self, name, price):
        Equipment.all_equipment += 1
        Xerox.counter += 1
        self.price = price
        self.name = name
        self.location = None

    def stock(self):
        Stock.items['Xerox'].append({self.name: self.price})
        Stock.items['Xerox'][0] += 1
        self.location = 'Stock'

    def move(self, where):
        self.location = where
        Stock.items['Xerox'].remove({self.name: self.price})
        Stock.items['Xerox'][0] -= 1


Epson = Printer('Epson', 23423)
Epson.stock()
Stock.count('Printer')
Epson.move('NPL-11')
Stock.count('Printer')