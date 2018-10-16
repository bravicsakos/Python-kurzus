#!/usr/bin/env python3


def szamjegyosszeg(li):
    lis2 = []
    for i in li:
        lis1 = list(str(i))
        for s in lis1:
            lis2.append(int(s))
    return sum(lis2)


def main():
    print(sum([i for i in range(101)]))
    print(szamjegyosszeg([10, 11, 12]))

#############################################################################


if __name__ == "__main__":
    main()