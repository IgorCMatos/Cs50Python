def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")

def is_valid(s):

    if not s[:1].isalpha():
        return False

    if not 2 <= len(s) <= 6:
        return False

    if not s.isalnum():
        return False

    for index in range(len(s)):

        if s[index].isdigit():
            if not s[index:].isdigit():
                return False

        if s[index].isalpha() == False:
            if s[index] == '0':
                return False
            else:
                return True

    return True

if __name__ == "__main__":
    main()
