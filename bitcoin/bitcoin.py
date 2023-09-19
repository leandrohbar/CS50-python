import sys
import requests


def main():
    if len(sys.argv) != 2:  # Check for command-line argument
        sys.exit("Missing command-line argument  ")
    try:
        bit = float(sys.argv[1])  # Check if command-line argument is a number
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:  # If command-line argument is a number, call bitcoin_value function
        bitcoin_value(bit)


def bitcoin_value(b):
    try:
        # Get current bitcoin value in USD
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rj = r.json()  # Convert to JSON
        usd = rj["bpi"]["USD"]["rate"].replace(",", "")  # Get USD value

        print(f"${float(usd) * b:,.4f}")  # Print bitcoin value in USD
    except requests.exceptions.JSONDecodeError:
        sys.exit()


if __name__ == "__main__":
    main()
