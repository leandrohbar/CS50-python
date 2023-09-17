def main():
    var = str(input("Type a variable in camelCase: ")).strip()
    replace_var(var)


def replace_var(c):
    # verify all the letters to convert from camel case to snake_case
    for i in range(len(c)):
        if c[i].isupper():
            print(
                f"_{c[i].lower()}", sep="", end=""
            )  # print the letter in lower case followed by the underscore
        else:
            print(c[i], sep="", end="")  # just print the letter if its not upper
    print()


main()
