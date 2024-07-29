import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):

        url = re.search(r"(https?:\/\/(www\.)*youtube\.com\/embed\/)([0-9_A-Z_a-z]+)", s)

        if url:
            split = url.groups()
            result = "https://youtu.be/" + split[2]
            return result

if __name__ == "__main__":
    main()
