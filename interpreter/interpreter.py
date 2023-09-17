def main():
    expression = input("Expression: ").strip().lower()
    math(expression)


def math(calc):
    # divide the expression to separete the 3 values
    x, y, z = calc.split(" ")

    # do the math operations
    match y:
        case "*":
            print(float(x) * float(z))
        case "/":
            print(float(x) / float(z))
        case "+":
            print(float(x) + float(z))
        case "-":
            print(float(x) - float(z))


main()
