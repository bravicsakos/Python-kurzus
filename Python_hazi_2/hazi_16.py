#!/usr/bin/env python3
# encoding: utf-8


def tisztit(s):
    s1 = ""
    i = 0
    while i < len(s):
        if not s[i].isspace():
            s1 += s[i]
        i += 1
    return s1


def main():
    s = "206.130.99.82:\n8080"
    print(tisztit(s))


##############################################################################

if __name__ == "__main__":
    main()
