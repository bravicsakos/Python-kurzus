#!/usr/bin/env python3
# encoding: utf-8


def main():
    s = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!   

Aqmimjjyi:

Ynyb"""
    s1 = """"""
    i = 0
    while i < len(s):
        if s[i].isalpha():
            if s[i] == 'y':
                s1 += 'a'
            elif s[i] == 'z':
                s1 += 'b'
            elif s[i] == 'Y':
                s1 += 'A'
            elif s[i] == 'Z':
                s1 += 'B'
            else:
                s1 += chr(ord(s[i])+2)
        else:
            s1 += s[i]
        i += 1
    print(s1)


##############################################################################

if __name__ == "__main__":
    main()
