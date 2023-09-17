import inflect


def main():
    names = input_user() # gets a list of names from the user
    grammar(names) # prints a farewell message


def input_user(): # returns a list of names
    names = []
    while True:
        try:
            names.append(input("Name: ").strip().title()) # strip() removes whitespace
        except EOFError: # EOFError is raised when input() hits EOF
            return names


def grammar(nams): # takes a list of names and prints a farewell message
    p = inflect.engine() # inflect is a library that pluralizes words
    n = p.join((nams))

    print(f"Adieu, adieu, to {n}")


if __name__ == "__main__":
    main()
