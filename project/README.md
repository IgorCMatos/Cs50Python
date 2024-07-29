# Python Minigames
#### Video Demo:  <URL https://youtu.be/cNwYYteKIBs>
#### Description:
This project is a collection of simple minigames implemented in Python, using random.

being: Guess a number , Rock Paper Scissor and Heads or tails.

## Authors

Name: [Igor Coderitch.]

Github: [Cs50Igor] / edX: [igor_136]

City, Country: [Campo Grande, Brazil ]

Date of the video : [09/03/24]

## How to Play

1. Clone this repository to your local environment.
2. Ensure you have Python installed on your system.
3. Run the `project.py` file.
4. Choose one of the available minigames by typing the corresponding number.
   - Guess the Number.
   - Rock, Paper, Scissor.
   - Heads or Tails.
5. Follow the on-screen instructions to play each minigame
6. At the end of each "round", you'll have the option to play again or exit.

## Mini-games

### Guess the Number

Try to guess a random number between 1 and 100.

### Rock, Paper, Scissors

Play the classic game of rock, paper, scissors against the computer.

### Heads or Tails

Make a bet on whether a coin will land heads up or tails up.

## Design Choices

1. Modular Functions: Each game is implemented as a separate function, allowing for easy maintenance and scalability. Also makes it straightforward to add new games in the future.
2. Input Validation: Is implemented to ensure that users enter valid input.This prevents the program from crashing due to unexpected input.

## File project.py
### Description of functions:

### main()

This function shows to the user 4 differents options for choose the games or exit the program, the loop will continue until the user chooses to a game or exit.

### guess_number() /  rock_scissor() / head_tails()

All these functions have a similar idea of ​​randomizing a number/word for the computer and then asking the user for a number/word (if the user enters a number/word outside the allowed range of numbers/words, the program will ask again), after this will use the __result() functions of each game to see the result and return to the respective game
the result, to finally print. At least the program will ask the user if they want to play again or return to the main menu.

### guess_results() /  rock_scissor_result() / head_tails_result()

This function takes the users and random numbers/words and compares to see if the result:


for guess_results: if the number is bigger, smaller or if it is the right number.


for rock_scissor_result: if the word is the same or if the user won or lost to the computer.


for head_tails_result: if the word is the same or different.


returning the result of each comparison to the respective function.

### not_again()

This function asks the user if he wants to play again or not, if the answer "n" will return true and if "y" will return false, where the user will break the chosen game loop and return to the main function or play again, this function will only stop if the user responds (y/n).

## File test_project.py
### Description:

This file contains tests for the function guess_results(), rock_scissor_result(), head_tails_result(). Where in each test function we will use assert to test if the result is correct.
