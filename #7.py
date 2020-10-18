class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        return f'{self.real} + {self.imaginary}i' if  self.imaginary > 0 else f'{self.real} - {abs(self.imaginary)}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)


number = ComplexNumber(1, -2)
number2 = ComplexNumber(3, 5)
suma = number + number2
multip = number * number2
print(suma, multip)
