str = input("camelCase:")
print("snake_case: ",end = "")

for letter in str:

    if letter.islower():
        print(letter,end="")
        
    else:
        letter = letter.lower()
        print("_" + letter, end= "")
print()
