#!/usr/bin/env python3


def main():
    li = [7,3,0,2,5,1,6,4]
    pos = [4, 6, 8, 10, 12, 14, 16, 18]
    temppos = -1
    print("+" + "-" * 21 + "+")
    for row in range(8):
        s = "|   . . . . . . . .   |"
        s1 = []
        for i in range(8):
            if 7 - li[i] == row:
                temppos = pos[i]
        for i in range(len(s)):
            if i == temppos:
                s1.append("Q")
            else:
                s1.append(s[i])
        print("".join(s1))
    print("+" + "-" * 21 + "+")


#############################################################################


if __name__ == "__main__":
    main()
