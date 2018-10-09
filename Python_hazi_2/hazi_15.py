#!/usr/bin/env python3
# coding: utf-8


def main():
    # megold 1
    i = 1
    osszeg = 0
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            osszeg += i
        i += 1
    print(osszeg)

    # megold 2
    print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))


##############################################################################

if __name__ == "__main__":
    main()
