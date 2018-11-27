#!/usr/bin/env python3


def check_sum(array2D):
    rownums = []
    for row in array2D:
        rownums.append(max(row) - min(row))
    return sum(rownums)


def main():
    array = []
    with open("Day02.txt") as file:
        for line in file:
            temparr = []
            for s in line.split():
                temparr.append(int(s))
            array.append(temparr)
    print(check_sum(array))

#############################################################################


if __name__ == "__main__":
    main()