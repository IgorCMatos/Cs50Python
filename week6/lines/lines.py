import sys

def main():
    check_len()
    check_py()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")
    count_lines(lines)

def check_len():
    len_argv = len(sys.argv)

    if len_argv > 2:
        sys.exit("Too many command-line arguments")
    if len_argv < 2:
        sys.exit("Too few command-line arguments")

def check_py():
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python File")

def check_blank_spaces(line):
    if line.lstrip().startswith("#"):
        return True
    if line.isspace():
        return True
    return False

def count_lines(lines):
    counter = 0
    for line in lines:
        if check_blank_spaces(line) == False:
            counter += 1
    print(counter)

if __name__ == "__main__":
    main()
