#!/usr/bin/env python3

TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.
A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.
A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

def main():
    ekez = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
    nemekez = "aeiooouuuAEIOOOUUU"
    d = {}
    li = []
    for i in range(len(ekez) - 1):
        d[ekez[i]] = nemekez[i]
    for c in TEXT:
        if d.get(c):
            li.append(d[c])
        else:
            li.append(c)
    print("".join(li))

#############################################################################


if __name__ == "__main__":
    main()