#!/usr/bin/env python3


def szamjegy(szam, hatvany):
    i = szam**hatvany
    s = f"{i}"
    return len(s)


def main():
    szam = 2
    hatvany = 256
    print(szamjegy(szam, hatvany))


##############################################################################

if __name__ == "__main__":
    main()
