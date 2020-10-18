class Stock:
    pass


class Equipment(Stock):
    all_equipment = 0


class Printer(Equipment):
    counter = 0

    def __init__(self, id, price):
        Equipment.all_equipment += 1
        Printer.counter += 1
        self.price = price
        self.id = id


class Scanner(Equipment):
    counter = 0

    def __init__(self, id, price):
        Equipment.all_equipment += 1
        Scanner.counter += 1
        self.price = price
        self.id = id


class Xerox(Equipment):
    counter = 0

    def __init__(self, id, price):
        Equipment.all_equipment += 1
        Xerox.counter += 1
        self.price = price
        self.id = id
