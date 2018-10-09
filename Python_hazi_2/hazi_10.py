#!/usr/bin/env python3
# encoding: utf-8


def szorzat(li):
    szorz = 1
    for i in li:
        szorz *= i
    return szorz


def main():
    li = {}
    print(szorzat(li))


##############################################################################

if __name__ == "__main__":
    main()
