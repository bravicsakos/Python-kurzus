#!/usr/bin/env python3


def szokozrovidit(s):
    """Torli a felesleges extra szokozoket

    Végigmegy a kapott string betűin:
    -Amennyiben szóközt talál elmenti a szokoz valtozóban és hozzáadja az snew stringhez,
    -Amennyiben már talált szóközt és újabbat talál nem csinál semmit
    -Ha talált már szóközt és más karaktert talál elfelejti a talált szóközt
    -Ha nincs mentett szóköz és más karaktert talált szimplán elmenti
    -Visszatér az új stringgel
    """
    szokoz = False
    snew = ""
    for c in s:
        if c == " " and not szokoz:
            szokoz = True
            snew += c
        elif c != " " and szokoz:
            szokoz = False
            snew += c
        elif c != " " and not szokoz:
            snew += c
    return snew


def main():
    print(szokozrovidit('I  love   Python'))

#############################################################################


if __name__ == "__main__":
    main()
