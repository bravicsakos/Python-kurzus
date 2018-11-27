#!/usr/bin/env python3


def run_maze(arrray):
    position = 0
    jumps = 0
    while 0 <= position < len(arrray):
        arrray[position] += 1
        position += arrray[position] - 1
        jumps += 1
    return jumps


def main():
    array = []
    with open("Day05.txt") as file:
        for line in file:
            array.append(int(line))
    print(run_maze(array))

#############################################################################


if __name__ == "__main__":
    main()