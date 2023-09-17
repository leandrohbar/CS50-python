def main():
    # prompt the user for a file name
    ext = input("Type a file name: ").strip().lower()
    # call a function to determine what is the name of the file
    extension(ext)


def extension(ext):
    # check each type of files and return the web type of it
    if ".gif" in ext:
        print("image/gif")
    elif ".jpg" in ext:
        print("image/jpeg")
    elif ".jpeg" in ext:
        print("image/jpeg")
    elif ".png" in ext:
        print("image/png")
    elif ".pdf" in ext:
        print("application/pdf")
    elif ".txt" in ext:
        print("text/plain")
    elif ".zip" in ext:
        print("application/zip")
    else:
        print("application/octet-stream")


main()
