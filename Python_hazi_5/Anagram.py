#!/usr/bin/env python3


def normalize(s):
    """
    A kapott string-nek visszaadja a normalizált alakját
    amely csak kisbetűket tartalmaz.
    """
    s1 = []
    for c in s:
        if c.isalpha():
            s1.append(c.lower())
    return "".join(s1)


def isanagram1(s1, s2):
    """
    Két string-ről eldönti hogy egymás anagrammái-e

    Dictionary-be gyűjti a különböző betűket a normalizált stringekből
    és előfordulásuk számát majd összehasonlítja a két dictionary-t
    """
    d1 = {}
    d2 = {}
    for c in normalize(s1):
        if d1.get(c):
            d1[c] += 1
        else:
            d1[c] = 1
    for c in normalize(s2):
        if d2.get(c):
            d2[c] += 1
        else:
            d2[c] = 1
    return d1 == d2


def isanagram2(s1, s2):
    """
    Két string-ről eldönti hogy egymás anagrammái-e

    Listát készít a két string normalizált változatából majd
    a két listát rendezve összehasonlítja őket
    """
    li1 = list(normalize(s1))
    li2 = list(normalize(s2))
    return sorted(li1) == sorted(li2)

def main():
    s1 = "Clint Eastwood"
    s2 = "Old west action"
    print(isanagram1(s1, s2))

#############################################################################


if __name__ == "__main__":
    main()
