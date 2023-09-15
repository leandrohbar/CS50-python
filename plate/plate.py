def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if max_min_char(s) == False:
        return False
    elif begining(s) == False:
        return False
    if numbers_end(s) == False:
        return False
    if psp_ver(s) == False:
        return False
    else:
        return True

# check the size of the plate
def max_min_char(plat_e):
    if len(plat_e) > 6 or len(plat_e) < 2:
        return False
    else:
        return True

# check if the 2 first char are letters
def begining(plat_e):
    return plat_e[0:2].isalpha()

# check the if the numbers (if there is) are at the end
def numbers_end(plat_e):
    if any(char.isdigit() for char in plat_e):
        found_digit = False
        numbers = ""
        for item in plat_e:
            if item.isdigit():
                numbers += item
                found_digit = True
            elif found_digit:
                return False

        return not numbers[0] == "0"
    else:
        return True

# check if there is any period, space or pontcuation
def psp_ver(plat_e):
    return plat_e.isalnum()

main()