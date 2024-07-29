
def main():
    Text = input("Input: ")
    Result = shorten(Text)
    print("Output: ",Result, end="")

def shorten(Text):

    Vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    Result_text = ""

    for letter in Text:

        if letter in Vowels:
            continue

        Result_text += letter

    return Result_text

if __name__ == "__main__":
    main()
