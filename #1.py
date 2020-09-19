from time import sleep


class TrafficLight:
    __color = [('красный', 2), ('желтый', 2), ('зеленый', 3)]

    def running(self):
        for a, b in self.__color:
            print(a)
            sleep(b)


c = TrafficLight()
c.running()
