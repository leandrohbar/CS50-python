import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        input_file = sys.argv[1]
        output_file = (
            sys.argv[2] + ".csv" if not sys.argv[2].endswith(".csv") else sys.argv[2]
        )

    writer_csv(input_file, output_file)


def check_csv_empty(filename):
    with open(filename,"r") as file:
        csv_reader = csv.reader(file)
        # Use next() to skip the header row if there is one
        next(csv_reader, None)
        # Check if there are any rows in the CSV
        if not any(row for row in csv_reader):
            raise Exception("The file is empty!")


def writer_csv(input_file, output_file):
    while True:
        try:
            check_csv_empty(input_file)  # Check if the file is empty

            with open(output_file, "w", newline="") as output_csv:
                writer = csv.DictWriter(
                    output_csv, fieldnames=["first", "last", "house"]
                )
                writer.writeheader() # Write the header

                with open(input_file, "r") as input_csv:
                    reader = csv.DictReader(input_csv)
                    for row in reader:
                        first = row["name"].split(", ")[1]
                        last = row["name"].split(", ")[0]
                        house = row["house"]
                        writer.writerow({"first": first, "last": last, "house": house})
            break

        except FileNotFoundError:  # File not found
            sys.exit(f"Could not read {sys.argv[1]}")
        except Exception as e:  # Empty file
            print(e)
            sys.exit(0)


if __name__ == "__main__":
    main()
