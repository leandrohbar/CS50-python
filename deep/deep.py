# prompt the user to answer
def main():
    answer = input(
        "What's the answer to the great question of life? the Universe, and Everything? "
    ).strip()
    get_answer(answer)


# call the function to decide what to answer
def get_answer(an):
    match an.lower():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()
