def main():

    time = input("What time is it? ")
    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("Breakfast time")

    elif 12.0 <= time <= 13.0:
        print("Lunch time")

    elif 18.0 <= time <= 19.0:
        print("Dinner time")

def convert(time):

    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) /60

    time = hours + minutes

    return time

if __name__ == "__main__":
    main()
