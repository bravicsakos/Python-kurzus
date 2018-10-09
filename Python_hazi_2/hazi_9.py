#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    l = ["y", "Y", "yes"]
    inp = input(f"Do you really want to quit ({l[0]}/{l[1]}/{l[2]})? ")
    if inp in l:  # <- egyszerűbben?
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')


##############################################################################

if __name__ == "__main__":
    main()
