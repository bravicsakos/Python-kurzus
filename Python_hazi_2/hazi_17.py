#!/usr/bin/env python3
# encoding: utf-8


def main():
    i = 32
    while i <= 127:
        print(f"{i}: {chr(i)}")
        i += 1


##############################################################################

if __name__ == "__main__":
    main()
