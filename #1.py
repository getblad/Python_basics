class Data:
    data = ''

    def __init__(self, date):
        Data.data = date

    @staticmethod
    def numbers(date):
        n = {}
        for i, v in enumerate(date.split('.')):
            n[i] = v
        return f'день {n[0]} из 31, месяц {n[1]} из 12' if int(n[0]) < 31 and int(n[1]) < 13 else None

    @classmethod
    def ints(cls):
        fn = {}
        for m, k in enumerate(cls.data.split('.')):
            fn[m] = k
        return fn[0], fn[1], fn[2]

    def my_method1(self):
        return (Data.numbers(Data.data), Data.ints()) if Data.numbers(Data.data) else 'Дата введена неверно'


d = Data('12.03.98')
print(d.my_method1())
