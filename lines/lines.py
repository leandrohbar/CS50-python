import sys


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(0)

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")

    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(0)

    else:
        l = open_file()
        print(f"{len(l)}")


def open_file():
    """
    Reads a file and returns a list of non-empty, non-comment lines.

    Returns:
    list: A list of non-empty, non-comment lines in the file.

    Raises:
    FileNotFoundError: If the file specified in the command line arguments does not exist.
    """
    lines = []
    while True:
        try:
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if not line.lstrip().startswith("#") and not line.isspace():
                        lines.append(line)

            return lines
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(0)


if __name__ == "__main__":
    main()