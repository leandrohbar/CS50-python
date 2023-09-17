def convert(emoji):
    emoji = emoji.replace(":)", "😀")
    emoji = emoji.replace(":(", "🙁")
    return emoji


def main():
    n = input("Type something: ")
    n = convert(n)
    print(n)


main()
