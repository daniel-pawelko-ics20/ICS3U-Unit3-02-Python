#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This is a guessing game


def main():
    # This function inputs guess and outputs if correct or not

    NUM = 4

    # input
    guess = int(input("Enter guess(0-9): "))

    # process/output
    if guess == NUM:
        print("You guessed correct!")
    elif guess < 0 or guess > 9:
        print("Please guess from 0-9")
    else:
        print("You guessed incorrectly :(")

    # output finished
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
