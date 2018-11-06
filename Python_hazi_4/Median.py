#!/usr/bin/env python3
import math


def median(li):
    """A li listának visszaadja a mediánját

    -Rendezi a listát egy új listaként, az eredeti sorrendjét meghagyva
    -Ha a lista elemeinek száma páratlan visszatér a hossz felének egész kitevőjével
    -Ha a lista elemeinek száma páros visszatér a a hossz felének és a hossz fele -1 elemnek az átlagával"""
    linew = li
    linew.sort()
    if len(linew) % 2 == 1:
        return linew[math.floor(len(linew) / 2)]
    else:
        return (linew[int(len(linew) / 2) - 1] + linew[int(len(linew) / 2)]) / 2


def main():
    li = [3, 6, 20, 99, 10, 15]
    print(median(li))

#############################################################################


if __name__ == "__main__":
    main()
