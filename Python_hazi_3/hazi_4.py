#!/usr/bin/env python3


def palin1(s1):
    s2 = s1[::-1]
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
                return False
        i += 1
    return True


def palin2(s):
    i = 0
    while i < len(s):
        if s[i] != s[len(s)-i-1]:
            return False
        i += 1
    return True


def palin3(s, i=0):
    if i == len(s):
        return True
    if s[i] == s[len(s)-i-1]:
        return palin3(s, i+1)
    else:
        return False


def main():
    s = "atttab"
    if palin3(s):
        print("YES")
    else:
        print("NO")


##############################################################################

if __name__ == "__main__":
    main()
