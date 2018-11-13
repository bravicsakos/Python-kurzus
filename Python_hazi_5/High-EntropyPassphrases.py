#!/usr/bin/env python3


def check(s):
    li = sorted(s.split())
    for i in range(len(li) - 1):
        if li[i] == li[i+1]:
            return False
    return True


def main():
    summ = 0
    with open("day04.txt", "r") as file:
        for line in file:
            if check(line):
                summ += 1
    print(summ)

#############################################################################


if __name__ == "__main__":
    main()