#!/usr/bin/env python3

import math


def dectobin(number):
    li = []
    while number > 0:
        li.append(number % 2)
        number = math.floor(number / 2)
    return li[::-1]


def main():
    a = 156
    print(dectobin(a))

#############################################################################


if __name__ == "__main__":
    main()
