#!/usr/bin/env python3


def spiral(length):
    mainli = [[None] * length for j in range(length)]
    pos_x = 0
    pos_y = 0
    incr_x = 1
    incr_y = 0
    for i in range(1, length*length + 1):
        mainli[pos_x][pos_y] = i
        temp_x = pos_x + incr_x
        temp_y = pos_y + incr_y
        if 0 <= temp_x < length and 0 <= temp_y < length and mainli[temp_x][temp_y] is None:
            pos_x = temp_x
            pos_y = temp_y
        else:
            incr_x, incr_y= - incr_y, incr_x
            pos_x += incr_x
            pos_y += incr_y
    print_spiral(mainli)


def print_spiral(array):
    for y in range(len(array)):
        for x in range(len(array)):
            if array[x][y] > 9:
                print(f" {array[x][y]} ", end="")
            else:
                print(f"  {array[x][y]} ", end="")
        print()


def main():
    spiral(5)


#############################################################################


if __name__ == "__main__":
    main()
