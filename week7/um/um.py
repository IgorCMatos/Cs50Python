import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    pattern = re.findall(r"\bum\b", s, re.IGNORECASE)
    len_um = len(pattern)
    return len_um

if __name__ == "__main__":
    main()

