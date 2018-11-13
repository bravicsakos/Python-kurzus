#!/usr/bin/env python3


def works(s):
    """
    Megállapítja hogy a zárójelek helyesek e az s stringben

    Egy dictionary-t használva feltölt egy listát a nyitó zárójelekkel és amennyiben talál
    egy zárót ha az egyezik az utolsó nyitóval akkor törli a listából és megy tovább.
    """
    di = {")" : "(", "}" : "{", "]" : "["}
    li = []
    for c in s:
        if c in di.values():
            li.append(c)
        elif c in di.keys():
            if di[c] == li[len(li) - 1]:
                li.pop(len(li) - 1)
            else:
                return False
    if len(li) == 0:
        return True
    return False


def main():
    print(works("(({[(((1)-2)+3)-3]/3}-3)"))


#############################################################################


if __name__ == "__main__":
    main()