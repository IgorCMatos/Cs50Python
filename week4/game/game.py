import random

while True:
    try:
        user_level = int(input("Level:"))

        if user_level > 0:
            random_level = random.randint(1, user_level)
            break

    except ValueError:
        pass

while True:
    try:
        user_number = int(input("Guess: "))

        if user_number == random_level:
            print("Just right!")
            break
        elif user_number > random_level:
            print("Too large!")
        else:
            print("Too small!")

    except ValueError:
        pass

