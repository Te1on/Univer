import numpy as np


class Affine:
    def __init__(self, m, v):
        self.m = m
        self.v = v

    def transform(self, x):
        return x @ self.m + self.v

    def __add__(self, other):
        return Affine(np.array(other.m) @ np.array(self.m),
                      np.array(other.v) @ np.array(self.m) + np.array(self.v))

    def __repr__(self):
        return str(np.array(self.m).round(decimals=2)) + "x + " + str(np.array(self.v))


if __name__ == "__main__":
    aff1 = Affine([[2, 0], [0, 2]], [5, -5])
    x = np.array([10, 10])
    print(aff1.transform(x))
    phi = np.pi/2
    aff2 = Affine([[np.cos(phi), np.sin(phi)], [-np.sin(phi), np.cos(phi)]], [0, 0])
    print(aff2.transform(x))
    aff3 = aff1 + aff2
    print(aff3.transform(x))
    print(aff3)

