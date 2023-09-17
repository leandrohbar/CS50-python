def main():
    # call the function that is gonna erase the vowels
    phrase = str(input("Type any phrase: "))
    vowel_out(phrase)


def vowel_out(p):
    vowels = ["a", "e", "i", "o", "u"]  # creates a list of the vowels

    # check and ignore any vowels
    new_word = []
    for i in range(len(p)):
        if p[i].lower() not in vowels:
            new_word.append(p[i])

    # add the letter besides any vowel to a new variable and print it
    new_word = "".join(new_word)
    print(new_word)


main()
