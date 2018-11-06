#!/usr/bin/env python3
import random

number = random.randint(1, 100)
guesses = 0


def inp():
    """Rekurzív függvény amely inputot kér be és azt kezeli

    -Növeli a guesses-t
    -Ha az input megegyezik a számmal: kiírja a sikert és a próbálkozások számát (guesses)
    -Ha az input kisebb/nagyobb a számnál: kiírja hogy kisebb/nagyobb és újra meghívja önmagát
    """
    i = int(input("your guess> "))
    guesses += 1
    global guesses
    if i == number:
        print("Good job! That's it!")
        print(f"Number of guesses: {guesses}")
    elif i > number:
        print("my number is smaller")
        inp()
    elif i < number:
        print("my number is larger")
        inp()


def main():
    print("Number Guessing Game")
    print("-" * 20)
    print("I thought of a number between 1 and 100.")
    # print(f"#debug: the number is {number}")
    inp()


#############################################################################


if __name__ == "__main__":
    main()
