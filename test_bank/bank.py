def main():
    # prompt the user to type waht the greeting is
    gret = input("Say some greeting: ")
    # call the function to calculate the payment
    pay = value(gret)
    print(f"${pay}")

def value(greeting):
        #check each of the 3 possibilities
        if  "hello" in greeting.lower().split()[0]:
            return 0
        elif greeting.lower().find("h") == 0:
            return 20
        else:
            return 100

if __name__ == "__main__":
     main()