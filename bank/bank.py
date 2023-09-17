def main():
    # prompt the user to type waht the greeting is
    gret = input("Say some greeting: ").strip().lower()
    # call the function to calculate the payment
    pay = greeting(gret)
    print(f"${pay}")


def greeting(g):
    # check each of the 3 possibilities
    if "hello" in g.split()[0]:
        return 0
    elif g.find("h") == 0:
        return 20
    else:
        return 100


main()
