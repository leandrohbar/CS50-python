import random


def main():
    lev = get_input()  # get level
    guess = get_random(lev)  # get random number
    guessed(guess)


def get_input():
    while True:
        try:
            level = int(input("Level: "))  # get level
            if level < 1:  # if level is less than 1,
                continue
            else:
                return level  # return level
        except ValueError:  # if input is not a number,
            pass


def get_random(l):
    levels = [i + 1 for i in range(l)]  # create list of numbers from 1 to level
    guess = random.choice(levels)  # choose random number from list
    return guess


def guessed(g):
    while True:
        try:
            num = int(input("Guess: "))  # get guess
            if num < 1:
                continue
            else:
                if num < g:  # if guess is less than random number, print "Too small!"
                    print("Too small!")
                elif num > g:  # if guess is greater than random number, print "Too large!"
                    print("Too large!")
                else:  # if guess is equal to random number, print "Just right!"
                    print("Just right!")
                    return
        except ValueError:
            pass


if __name__ == "__main__":
    main()
