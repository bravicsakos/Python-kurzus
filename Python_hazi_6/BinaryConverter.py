#!/usr/bin/env python3

def convert(s):
    osszeg = 0
    count = 0
    for c in s:
        if c == "1":
            if count == 0:
                osszeg += 128
            else:
                osszeg += 128 / (2**count)
        count += 1
    return osszeg


def main():
    sli = ["01111001", "01101111", "01110101", "01110100", "01110101", "00101110", "01100010", "01100101",
           "00101111", "01100100", "01010001", "01110111", "00110100", "01110111", "00111001", "01010111",
           "01100111", "01011000", "01100011", "01010001"]
    for s in sli:
        print(chr(int(convert(s))), end="")


#############################################################################


if __name__ == "__main__":
    main()