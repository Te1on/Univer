class Polynom:
    def __init__(self, *coef):
        self.coef = coef

    def __repr__(self):
        pp = ""
        for i in range(len(self.coef)):
            if self.coef[i] != 0:
                pp += str(self.coef[i])
                if i != 0:
                    pp += "x^"+str(i)
                if i < len(self.coef) - 1:
                    if self.coef[i+1] >= 0:
                        pp += "+"

        return pp

    def __add__(self, other):
        c1 = list(self.coef)
        c2 = list(other.coef)

        len1 = len(self.coef)
        len2 = len(other.coef)
        maxlen = len1
        if len1 > len2:
            c2.extend([0] * (len1 - len2))
            maxlen = len1
        elif len1 < len2:
            c1.extend([0] * (len2 - len1))
            maxlen = len2

        return Polynom(*[c1[i] + c2[i] for i in range(maxlen)])

    def __sub__(self, other):
        c1 = list(self.coef)
        c2 = list(other.coef)

        len1 = len(self.coef)
        len2 = len(other.coef)
        maxlen = len1
        if len1 > len2:
            c2.extend([0] * (len1 - len2))
            maxlen = len1
        elif len1 < len2:
            c1.extend([0] * (len2 - len1))
            maxlen = len2

        return Polynom(*[c1[i] - c2[i] for i in range(maxlen)])

    def __mul__(self, other):
        c1 = list(self.coef)
        c2 = list(other.coef)
        res = [0] * (len(c1) + len(c2) - 1)
        for o1, i1 in enumerate(c1):
            for o2, i2 in enumerate(c2):
                res[o1 + o2] += i1 * i2
        return Polynom(*res)


if __name__ == "__main__":
    y = Polynom(1,1)
    x = Polynom(1,-1)
    print(y + x)
    print(y - x)
    print(y * x)

