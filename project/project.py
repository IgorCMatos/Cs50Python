import random

def main():
    while True:
        print("Choose a Minigame")
        choose_game = input("What would you like to play? \n1-Guess a number \n2-rock, paper, scissor \n3-Heads or Tails \n4-Exit\n").strip()
        match choose_game:
            case "1":
                guess_number()
            case "2":
                rock_scissor()
            case "3":
                head_tails()
            case "4":
                print("Bye!! See you later")
                break
            case _:
                print("Invalid Choice. Please choose again.")

def guess_number():
    random_number = random.randint(1, 100)

    while True:
        while True:
            try:
                user_guess = int(input("Guess a number between 1 and 100: "))
                if 1 <= user_guess <= 100:
                    break
                else:
                    print("Please enter a number from 1 to 100.")
            except ValueError:
                print("Enter a valid number.")

        result = guess_results(user_guess, random_number)
        print(result)

        if result == "You Won!!":
            if not_again():
                break
            else:
                random_number = random.randint(1, 100)

def guess_results(user_guess, random_number):
    if user_guess > random_number:
        return "Number Too High. Try again."
    elif user_guess < random_number:
        return "Number Too Low. Try again."
    else:
        return "You Won!!"

def rock_scissor():

    while True:
        user_hand = input("What do you choose? Type Rock, Paper or Scissor: ").lower().strip()
        if user_hand not in ["rock", "paper", "scissor"]:
            print("Please enter Rock, Paper or Scissor.")
            continue

        computer_hand = random.choice(["rock", "paper", "scissor"])
        result = rock_scissor_result(user_hand, computer_hand)
        print(result)

        if not_again():
            break
        else:
            computer_hand = random.choice(["rock", "paper", "scissor"])

def rock_scissor_result(user_hand, computer_hand):
    if user_hand == computer_hand:
        return f"It's a tie, the computer chose: {computer_hand}"
    elif (user_hand == "rock" and computer_hand == "scissor") or  (user_hand == "paper" and computer_hand == "rock") or (user_hand == "scissor" and computer_hand == "paper"):
        return f"You won, the computer chose: {computer_hand}"
    else:
        return f"You lost, the computer chose: {computer_hand}"

def head_tails():

    while True:
        user_choice = input("Heads or Tails? (heads/tails): ").lower().strip()
        if user_choice not in ["heads", "tails"]:
            print("Please enter heads or tails.")
            continue

        coin = random.choice(["heads", "tails"])

        result = head_tails_result(user_choice, coin)
        print(result)

        if not_again():
            break

def head_tails_result(user_choice, coin):
    if user_choice == coin:
        return "You won!!!"
    else:
        return f"You lost! The coin side was {coin}."

def not_again():
    while True:
        user_input = input("Do you want to play again? (y/n): ").lower()
        if user_input == "n":
            return True
        elif user_input == "y":
            return False
        else:
            print("Please enter y or n.")

if __name__ == "__main__":
    main()
