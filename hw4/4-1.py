class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.imag != 0 and self.real != 0:
            return str(self.real) + " + " + str(self.imag) + "i"
        elif self.real == 0:
            return str(self.imag) + "i"
        else:
            return str(self.real)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)


if __name__ == "__main__":
    a = Complex(2, 1)
    #print(a)
    b = Complex(1, 1)
    print(a + b)
    print(a - b)
    print(a * b)
