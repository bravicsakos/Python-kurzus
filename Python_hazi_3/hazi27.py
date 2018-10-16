#!/usr/bin/env python3
# coding: utf-8


def hangrend(word):
    MELY = 'aáoóuú'
    MAGAS = 'eéiíöőüű'
    mely = False
    magas = False
    for c in word:
        if MELY.find(c) != -1:
            mely = True
        if MAGAS.find(c) != -1:
            magas = True
    if magas and mely:
        return "Vegyes"
    elif mely:
        return "Mely"
    else:
        return "Magas"

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    print([hangrend(s) for s in words])


#############################################################################


if __name__ == "__main__":
    main()
