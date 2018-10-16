#!/usr/bin/env python3


def XOR(obj1, obj2):
    if bool(obj1) and not bool(obj2):
        return True
    elif not bool(obj1) and bool(obj2):
        return True
    else:
        return False

def main():
    s1 = None
    s2 = []
    if XOR(s1, s2):
        print("YES")
    else:
        print("NO")

#############################################################################


if __name__ == "__main__":
    main()
