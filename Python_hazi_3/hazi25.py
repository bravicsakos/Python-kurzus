#!/usr/bin/env python3

import math


def gyemantosito(magassag):
    if magassag % 2 == 0:
        print("""Rossz érték gyémántosítónál:
            várt: páratlan
            kapott: páros""")
        return
    i = 1
    hossz = 1
    lis = [szam for szam in range(1000) if szam % 2 == 1]
    maxhossz = lis[math.ceil(magassag/2)]
    while i <= math.ceil(magassag/2):
        s = ""
        j = 1
        while j <= hossz:
            s += "*"
            j += 1
        print(s.center(maxhossz))
        hossz += 2
        i += 1
    hossz -= 4
    while i <= magassag:
        s = ""
        j = 1
        while j <= hossz:
            s += "*"
            j += 1
        print(s.center(maxhossz))
        hossz -= 2
        i += 1


def main():
    gyemantosito(4)

#############################################################################


if __name__ == "__main__":
    main()
