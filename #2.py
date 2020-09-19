class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, thickness, mass_sm):
        return self._length*self._width*thickness*mass_sm


Road_1 = Road(20, 5000)
print(Road_1.mass(25, 5))



