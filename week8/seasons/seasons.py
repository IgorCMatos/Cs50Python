from datetime import date
import inflect
import sys
import re

p = inflect.engine()

def main():

        try:
             bdate = input("Date of Birth: ")
             year, month, day = valid_date(bdate)
        except:
             sys.exit("Invalid date")

        print(f"{calculate_minutes(year, month,day)} minutes")

def valid_date(bdate):

     if re.search(r"[0-9]{4}-[0-9]{2}-[0-9]{2}",bdate):
          year, month, day = bdate.split("-")
          return year, month, day

def calculate_minutes(year, month, day):
     user_date = date(int(year), int(month), int(day))
     today_date = date.today()

     diference = today_date - user_date

     total = diference.days * 24 * 60
     minutes_in_words = p.number_to_words(total, andword = "")
     return minutes_in_words.capitalize()

if __name__ == "__main__":
    main()
