def main():
    percent = get_fraction("Fraction: ")  # Get the fraction
    print_percentage(percent)  # Print the percentage


def get_fraction(f):
    while True:  # Loop until a valid fraction is entered
        try:  # Try to convert the input to a fraction
            ff = input(f).split("/")
            x = int(ff[0])
            y = int(ff[1])
            if x <= y:  # Check if the fraction is valid
                return x / y
            else:
                continue
        except ValueError:  # If the input is not a fraction
            print("It must be a number fraction!")
        except ZeroDivisionError:  # If the denominator is 0
            pass


def print_percentage(p):  # Print the percentage
    if p * 100 <= 1:  # If the percentage is 1% or less
        print("E")
    elif p * 100 >= 99:  # If the percentage is 99% or more
        print("F")
    else:
        print(f"{round(p * 100)}%")  # Print the percentage


if __name__ == "__main__":
    main()
