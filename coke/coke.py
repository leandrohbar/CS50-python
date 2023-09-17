def main():
    put_coins()


def put_coins():
    # check what coin was inserted and the amount dued
    coke_price = 50
    while True:
        coins = int(input("Insert a coin: "))
        match coins:
            case 25:
                coke_price -= 25
            case 10:
                coke_price -= 10
            case 5:
                coke_price -= 5
            case _:
                print("Insert a valid coin!")
        if coke_price > 0:
            print(f"Amount Due: {coke_price}")
        elif coke_price <= 0:
            print(f"Change Owed: {coke_price * - 1}")
            break


main()
