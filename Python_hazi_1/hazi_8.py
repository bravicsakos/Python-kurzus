#!/usr/bin/env python3


def main():
    hazik = [("Hazi_1", 132, "Done"), ("Hazi_2", 115, "Done"),
             ("Hazi_3", 26, "Done"), ("Hazi_4", 44, "Done"),
             ("Hazi_5", 19, "Done"), ("Hazi_6", 20, "Done"),
             ("Hazi_7", 18, "Done"), ("Hazi_8", 21, "Done")]

    print("{0:<8} {1:<12} {2:<8}".format("Nev", "Sorok szama", "Allapot"))

    print("-"*28)
    for element in hazik:
        print("{0:<8} {1:<12} {2:<8}".format(element[0], element[1], element[2]))


##############################################################################

if __name__ == "__main__":
    main()
