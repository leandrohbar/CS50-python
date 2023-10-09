import sys
from PIL import Image, ImageOps
import os.path


def main():
    # Check for correct usage
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Check if input is valid
        ext = os.path.splitext(sys.argv[1])
        if ext[1].lower() != ".jpg" and ext[1].lower() != ".jpeg" and ext[1].lower() != ".png":
            sys.exit("Invalid input")
        
        # Check for correct output
        ext = os.path.splitext(sys.argv[2])
        if ext[1].lower() != ".jpg" and ext[1].lower() != ".jpeg" and ext[1].lower() != ".png":
            sys.exit("Invalid output")

        # Check if input and output have same extension
        if os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
            sys.exit("Input and output have different extensions")


    try: # Open shirt image
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt image does not exist")

    try: # Open output image
        input = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    
    size = shirt.size # Resize input to shirt size
    output = ImageOps.fit(input, size)

    output.paste(shirt, mask=shirt)
    output.save(sys.argv[2])

if __name__ == "__main__":
    main()
