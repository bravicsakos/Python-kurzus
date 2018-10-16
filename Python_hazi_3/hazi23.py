#!/usr/bin/env python3


def main():
    li1 = "the quick brown fox jumps over the lazy frog"
    lo1 = [(s, len(s)) for s in li1.split()]
    print(lo1)
    lo2 = [i for i in range(10) if i % 2 == 0]
    print(lo2)
    lo3 = [i*i for i in range(20) if (i*i) % 10 == 4]
    print(lo3)
    lo4 = [chr(i) for i in range(65, 91)]
    s1 = ""
    for c in lo4:
        s1 += c
    print(s1)
    li5 = [' apple ', ' banana ', ' kiwi']
    lo5 = [s.strip() for s in li5]
    print(lo5)
    s2 = ""
    li6 = [1, 0, 1, 1, 0, 1, 0, 0]
    for i in li6:
        s2 += str(i)
    print(s2)

#############################################################################


if __name__ == "__main__":
    main()
