class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


a = Stationery('Рисунок1')
a.draw()
b = Pen('Рисунок2')
b.draw()
c = Pencil('Рисунок3')
c.draw()
d = Handle('Рисунок4')
d.draw()
