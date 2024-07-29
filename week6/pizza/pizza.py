from tabulate import tabulate
import csv
import sys

def main():
    check_len()
    check_csv()
    create_table()

def check_len():
    len_argv = len(sys.argv)

    if len_argv > 2:
        sys.exit("Too many command-line arguments")
    if len_argv < 2:
        sys.exit("Too few command-line arguments")

def check_csv():
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV File")

def create_table():
    table = []

    try:
        with open(sys.argv[1], "r") as csvfile:
            read = csv.reader(csvfile)
            for row in read:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    table = tabulate(table, tablefmt="grid", headers ="firstrow")
    print(table)

if __name__ =="__main__":
    main()
