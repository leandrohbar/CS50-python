def main():
    date = get_input()
    print_date(date)


def get_input():  # get input from user
    while True:
        try:
            d = input("Date: ").title()
            d = format_date(d)
            if d is False:
                continue
            else:
                return d
        except EOFError:
            break


def format_date(date):  # format date to YYYY-MM-DD
    if "/" in date:  # if date is in format "MM/DD/YYYY"
        date_num = date.split("/")
        if date_num[0].isalpha():  # if month is invalid
            return False
    elif "," in date:  # if date is in format "Month DD, YYYY"
        date = date.replace(",", "")  # remove comma
        date_num = date.split(" ")  # split date into list
    else:
        return False

    # check if date is valid
    date_num = confirm_day(date_num)
    if date_num is False:
        return False
    # check if month is valid
    verify_m = confirm_month(date_num)

    if verify_m is False:  # if month is invalid
        return False
    else:
        date_num[0] = verify_m  # replace month with numeric value
        return date_num


def confirm_day(d):
    if d[1].isalpha():  # if day is invalid
        return False
    elif int(d[1]) < 1 or int(d[1]) > 31:  # if day is invalid
        return False
    else:
        return d


def confirm_month(month):  # month[0] = month, month[1] = day, month[2] = year
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # check if numeric, wether is a valid month
    if month[0] in months:
        return months.index(month[0]) + 1  # return numeric value of month
    elif int(month[0]) >= 1 and int(month[0]) <= 12:  # if month is numeric
        return month[0]
    else:
        return False


def print_date(dat):  # dat[0] = month, dat[1] = day, dat[2] = year
    print(f"{int(dat[2])}-{int(dat[0]):02}-{int(dat[1]):02}")


if __name__ == "__main__":
    main()
