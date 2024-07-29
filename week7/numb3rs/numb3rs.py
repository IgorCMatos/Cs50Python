import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split('.')

        for num in numbers:
            num = int(num)
            if num > 255:
                return False
            if num < 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
