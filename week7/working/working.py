import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    user_times = re.search(r"^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$", s)

    if user_times:
        split_time = user_times.groups()

        num1 = print_h(split_time[0], split_time[1], split_time[2])
        num2 = print_h(split_time[3], split_time[4], split_time[5])

        return num1 + " to " + num2
    else:
        raise ValueError

def print_h(hour, minute, daytime):
    if int(hour) == 12:
        if daytime == "AM":
            hour = 0
        else:
            hour = 12

    elif daytime == "PM":
        hour = int(hour) + 12

    if minute is None:
        minute = "00"

    new_time = f"{int(hour):02d}:{minute}"

    return new_time

if __name__ == "__main__":
    main()
