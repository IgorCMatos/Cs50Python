
Text = input("Input: ")
Vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

print("Output: ", end="")

for letter in Text:

    if letter in Vowels:
        continue

    print(letter, end="")

print()
