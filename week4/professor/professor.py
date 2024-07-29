import random

def main():
    user_level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(user_level)
        score += game(x, y)

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            user_level = int(input("Level: "))
            if 0 < user_level < 4:
                return user_level

        except ValueError:
            pass

def generate_integer(user_level):
    if user_level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif user_level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif user_level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def game(x, y):
    trys = 0
    while trys < 3:
        try:
            question = int(input(f"{x} + {y} = "))

            if question == x + y:
                return 1
            else:
                trys += 1
                print("EEE")

        except ValueError:
            trys += 1
            print("EEE")
            
    print(f"Correct answer: {x} + {y} = {x + y}")
    return 0

if __name__ == "__main__":
    main()
