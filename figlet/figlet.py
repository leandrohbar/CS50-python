import sys
from pyfiglet import Figlet
import random


def main():
    if len(sys.argv) == 3: # Two arguments
        verify_argv()
        print_font()
    elif len(sys.argv) == 1: # No arguments
        print_random()
    else:
        sys.exit("Invalid usage")


def verify_argv():
    function = Figlet() # Create Figlet object
    fonts = function.getFonts() # Get all fonts

    if sys.argv[1] != "-f" and sys.argv[1] != "--font": # -f or --font
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts: # Check if font is valid
        sys.exit("Invalid usage")
    else:
        return


def print_random():
    function = Figlet()
    fonts = function.getFonts()

    ran = random.choice(fonts) # Random font
    function.setFont(font=ran) # Set font
    inp = input("Input: ")
    print(function.renderText(inp))


def print_font():
    function = Figlet()
    function.setFont(font=sys.argv[2]) # Set font

    inp = input("Input: ")
    print(function.renderText(inp))


if __name__ == "__main__":
    main()
