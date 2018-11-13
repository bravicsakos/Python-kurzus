#!/usr/bin/env python3


def getpi(n):
    """
    Visszaadja a PI értékét n ciklus közelítés után
    """
    temp = 0
    odds = []
    start = 1
    for i in range(n):
        if i % 2 == 1:
            odds.append(start * -1)
        else:
            odds.append(start)
        start += 2
    for i in odds:
        temp += 1/i
    return 4 * temp


def main():
    print(getpi(376843))

#############################################################################


if __name__ == "__main__":
    main()