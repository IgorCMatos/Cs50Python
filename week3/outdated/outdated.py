Months = [
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
    "December"
]

def format_date_int(Date):
    try:
        Month, Day, Year = Date.split("/")

        Int_day = int(Day)
        Int_month = int(Month.replace(" ", ""))
        Year = int(Year.replace(" ", ""))

        if 1 <= Int_day <= 31 and  1 <= Int_month <= 12:
            return f"{Year}-{Int_month:02}-{Int_day:02}"

    except:
        pass

def format_date_str(Date):
    try:
        if "," not in Date:
            raise SyntaxError

        Month_str, Day_str, Year = Date.split(" ")

        for i in range(len(Months)):
            if Month_str == Months[i]:
                Month = i + 1

        Day = Day_str.replace(",", "")
        Int_day = int(Day)
        Int_month = int(Month)

        if 1 <= Int_day <= 31 and  1 <= Int_month <= 12:
            return f"{Year}-{Int_month:02}-{Int_day:02}"

    except:
        pass

while True:
    Date = input("Date: ")

    Result = format_date_int(Date)
    if Result:
        print(Result)
        break

    Result = format_date_str(Date)
    if Result:
        print(Result)
        break
