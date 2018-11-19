#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.li = []

    def ures(self):
        if self.li:
            return False
        return True

    def betesz(self, num):
        self.li.append(num)

    def kivesz(self):
        if self.li:
            return self.li.pop()
        else:
            return None

    def meret(self):
        return len(self.li)

    def __str__(self):
        s = []
        for i in self.li:
            s.append(str(i))
            s.append(" ")
        return "[" + "".join(s)


class Sor:
    def __init__(self):
        self.li = []

    def ures(self):
        if self.li:
            return False
        return True

    def betesz(self, num):
        self.li.append(num)

    def kivesz(self):
        if self.li:
            i = self.li[len(self.li) - 1]
            self.li.remove(i)
            return i
        else:
            return None

    def meret(self):
        return len(self.li)

    def __str__(self):
        s = []
        for i in self.li:
            s.append(str(i))
            s.append(" ")
        return "[" + "".join(s)


def main():
    v = Sor()
    print(v)
    print(v.ures())
    v.betesz(4)
    v.betesz(1)
    v.betesz(4)
    v.kivesz()
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


#############################################################################


if __name__ == "__main__":
    main()