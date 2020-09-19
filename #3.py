income = {'worker1': {'wage': 10000, 'bonus': 5000}, 'worker2': {'wage': 20000, 'bonus': 5000}}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income[position]


class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}')

    def get_total_income(self):
        print(f'Общий доход {self._income["wage"]+self._income["bonus"]}')


a = Position("Иван", "Иванов", 'worker1')
a.get_full_name()
a.get_total_income()