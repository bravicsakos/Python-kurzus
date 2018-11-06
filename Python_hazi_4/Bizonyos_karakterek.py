#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """A textből a charsban tallható karakterek kivétele

    A textben található string karaktereit vizsgálva csak a charsban
    megadottt karakterek felhasználásával készíti el az új stringet.
    """
    s = ""
    for c in text:
        if c in chars:
            s += c
    return s


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

#############################################################################


if __name__ == "__main__":
    main()
