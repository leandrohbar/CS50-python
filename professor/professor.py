import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))  # ask for the level
            if lvl < 1 or lvl > 3:  # check if the level is between 1 and 3
                continue
            else:
                return lvl  # return the level
        except ValueError:  # if the input is not a number
            pass


def generate_integer(level):
    if level == 1:
        level_1()  # call the level 1 function
    elif level == 2:
        level_2()  # call the level 2 function
    elif level == 3:
        level_3()  # call the level 3 function


def level_1():
    score = 0  # set this to keep track of how much correct answers was get
    for i in range(10):
        num1 = random.randrange(1, 9, 1)  # choose a random number for the x
        num2 = random.randrange(1, 9, 1)  # choose a random number for the y

        tries = 0  # set this to keep track of the tries
        while True:
            if tries == 3:
                print(
                    f"{num1} + {num2} = {num1 + num2}"
                )  # print the correct answer after the 3 wrong tries
                break
            try:
                guess = int(input(f"{num1} + {num2} = "))  # ask for the answer
                if guess != (num1 + num2):
                    print("EEE")  # print these for each wrong answer
                    tries += 1
                    continue
                else:
                    score += 1
                    break
            except ValueError:  # if the input is not a number
                print("EEE")  # print for a non number type
                tries += 1
                pass

    print(f"Score: {score}")  # print the score


def level_2():
    score = 0  # set this to keep track of how much correct answers was get
    for i in range(10):
        num1 = random.randrange(10, 99, 1)  # choose a random number for the x
        num2 = random.randrange(10, 99, 1)  # choose a random number for the y

        tries = 0  # set this to keep track of the tries
        while True:
            if tries == 3:
                print(
                    f"{num1} + {num2} = {num1 + num2}"
                )  # print the correct answer after the 3 wrong tries
                break
            try:
                guess = int(input(f"{num1} + {num2} = "))
                if guess != (num1 + num2):
                    print("EEE")  # print these for each wrong answer
                    tries += 1
                    continue
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")  # print for a non number type
                tries += 1
                pass

    print(f"Score: {score}")


def level_3():
    score = 0  # set this to keep track of how much correct answers was get
    for i in range(10):
        num1 = random.randrange(100, 999, 1)  # choose a random number for the x
        num2 = random.randrange(100, 999, 1)  # choose a random number for the y

        tries = 0  # set this to keep track of the tries
        while True:
            if tries == 3:
                print(
                    f"{num1} + {num2} = {num1 + num2}"
                )  # print the correct answer after the 3 wrong tries
                break
            try:
                guess = int(input(f"{num1} + {num2} = "))
                if guess != (num1 + num2):
                    print("EEE")  # print these for each wrong answer
                    tries += 1
                    continue
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")  # print for a non number type
                tries += 1
                pass

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
