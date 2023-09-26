def main():
    while True:
        f = input("Fraction: ")
        percent = convert(f)  # Get the fraction
        if percent != None:
            break

    gas = gauge(percent)  # Print the percentage
    print(gas)


def convert(f):
    while True:  # Loop until a valid fraction is entered
        try:  # Try to convert the input to a fraction
            ff = f.split("/")
            x = int(ff[0])
            y = int(ff[1])
            division = round((x / y) * 100, 2)
            if x > y:
                raise ValueError
                # Check if the fraction is valid

        except ValueError:  # If the input is not a fraction
            break
        except ZeroDivisionError:  # If the denominator is 0
            break
        except IndexError:
            break
        else:
            return division  # Return the percentage


def gauge(p):  # Print the percentage
    if p <= 1:  # If the percentage is 1% or less
        return "E"
    elif p >= 99:  # If the percentage is 99% or more
        return "F"
    else:
        return p


if __name__ == "__main__":
    main()
