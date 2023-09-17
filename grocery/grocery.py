def main():
    items = get_item()  # get the items from the user
    list_item(items)  # print the items in the list


def get_item():
    list = []
    while True:
        try:
            item = input().upper().strip()
            list.append(item)
        except EOFError:
            print()
            return list


def list_item(l):  # l is the list of items
    groc = {}

    # group the same products in a dictionare
    for product in l:
        # if the product is not in the dictionary, add it with value 1, else add 1 to the value
        groc[product] = groc.get(product, 0) + 1

    # sort in alphabetic order
    sorted_list = sorted(groc.keys())  # get the keys of the dictionary and sort them
    groc_final = {
        key: groc[key] for key in sorted_list
    }  # create a new dictionary with the sorted keys

    # print the products and the quantity
    for i in groc_final:
        print(f"{groc_final[i]} {i}")  # print the quantity and the product


if __name__ == "__main__":
    main()
