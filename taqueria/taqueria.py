def main():
    print_total()


def print_total():  # Prints total of items
    summ = []  # List of prices
    while True:  # loops for input
        try:
            inp = input("Item: ").title()
            summ.append(get_item(inp))  # Adds price of item to list
            print(f"Total: ${sum(summ):.2f}")  # Prints total of items
        except EOFError:  # Ctrl+D
            print()
            break


def get_item(item):  # Returns price of item
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    if item in menu:
        return menu.get(item)  # Returns price of item
    else:
        return 0


if __name__ == "__main__":
    main()
