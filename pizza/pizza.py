import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:  # if no command-line arguments
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:  # if too many command-line arguments
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")  # if not a CSV file
    else:  # if a CSV file
        print_table(sys.argv[1])


def print_table(csv_file):
    while True:
        try:  # try to open the CSV file
            with open(csv_file) as csvfile:  # open the CSV file
                reader = csv.DictReader(csvfile)  # read the CSV file
                # print the CSV file as a table
                print(tabulate(reader, headers="keys", tablefmt="grid"))
            break
        except FileNotFoundError:  # if file not found
            sys.exit("File not found")


if __name__ == "__main__":
    main()
