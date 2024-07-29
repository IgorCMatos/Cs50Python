import csv
import sys

def main():
    check_len()
    check_csv()
    data_list = []
    slipt_file(data_list)
    write_in_file(data_list)

def check_len():
    len_argv = len(sys.argv)

    if len_argv > 3:
        sys.exit("Too many command-line arguments")
    if len_argv < 3:
        sys.exit("Too few command-line arguments")

def check_csv():
     for arg in sys.argv[1:]:
        if not arg.lower().endswith(".csv"):
            sys.exit("Not a CSV File")

def slipt_file(data_list):
    try:
        with open(sys.argv[1], "r") as file:
            read = csv.DictReader(file)
            for row in read:
                name_parts = row["name"].split(",")
                data_list.append({"First": name_parts[1].strip(), "Last": name_parts[0].strip(), "House": row["house"].strip()})

    except FileNotFoundError:
        sys.exit("File does not exist")

def write_in_file(data_list):
    with open(sys.argv[2], "w", newline='') as copy_file:
        write = csv.DictWriter(copy_file, fieldnames=["First", "Last", "House"])
        write.writerow({"First":"First", "Last":"Last", "House":"House"})

        for row in data_list:
            write.writerow({"First":row["First"], "Last":row["Last"], "House":row["House"]})

if __name__ == "__main__":
    main()
