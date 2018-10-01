#!/usr/bin/env python3


def megfordit(i):
    s = f"{i}"
    s = s[::-1]
    return int(s)


def main():
    i = 56789
    print(megfordit(i))


##############################################################################

if __name__ == "__main__":
    main()
