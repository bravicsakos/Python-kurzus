#!/usr/bin/env python3


def main():
    print(sum([i for i in range(101)])**2 - sum([i*i for i in range(101)]))


#############################################################################


if __name__ == "__main__":
    main()
