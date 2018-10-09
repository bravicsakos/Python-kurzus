#!/usr/bin/env python3
# encoding: utf-8


def szorzatrek(li, index, szorzat):
    szorzat *= li[index]
    index += 1
    if index < len(li):
        szorzat = szorzatrek(li, index, szorzat)
    return szorzat


def main():
    li = [1, 2, 3, 4, 5]
    print(szorzatrek(li, 0, 1))


##############################################################################

if __name__ == "__main__":
    main()
