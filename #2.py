class Clothes:
    def __init__(self, name):
        self.name = name


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def consumption(self):
        return f'Расход ткани на {self.name} составит {2 * self.height + 3}'


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def consumption(self):
        return f'Расход ткани на {self.name} составит {self.size / 6.5 + 0.5:.2f}'


My_costume = Costume('ASD', 29)
My_coat = Coat('Wary', 30)
print(My_costume.consumption)
print(My_coat.consumption)
