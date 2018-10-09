#!/usr/bin/env python3
# encoding: utf-8


def osszegrek(li, index, osszeg):
    osszeg += li[index]
    index += 1
    if index < len(li):
        osszeg = osszegrek(li, index, osszeg)
    return osszeg


def main():
    li = [1, 2, 3, 10]
    print(osszegrek(li, 0, 0))


##############################################################################

if __name__ == "__main__":
    main()
