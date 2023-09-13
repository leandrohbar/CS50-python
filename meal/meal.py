def main():
    hour = input("What time is it? ")
    time = convert(hour)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    # take the hour and minutes of what the user prompt
    h, m = time.split(":")
    m = float(m) / 60
    return float(h) + float(m)

if __name__ == "__main__":
    main()