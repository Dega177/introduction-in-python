class MyComplex:
    def __init__(self, data):
        self.complex = data

    def __str__(self):
        return f'{self.complex}'

    def __add__(self, other):
        return MyComplex((self.complex.real + other.complex.real) + (self.complex.imag + other.complex.imag) * 1j)

    def __mul__(self, other):
        return MyComplex((self.complex.real * other.complex.real - self.complex.imag * other.complex.imag)
                         + (self.complex.real * other.complex.imag + self.complex.imag * other.complex.real) * 1j)


a = MyComplex(1 + 1j)
b = MyComplex(1 + 4j)
print(a + b)
print(a * b)
