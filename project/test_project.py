from project import guess_results, rock_scissor_result ,head_tails_result

def main():
    test_guess_results()
    test_rock_scissor_result()
    test_head_tails_result()

def test_guess_results():
    assert guess_results(100, 100) == "You Won!!"
    assert guess_results(100, 10) == "Number Too High. Try again."
    assert guess_results(10, 100) == "Number Too Low. Try again."

def test_rock_scissor_result():
    assert rock_scissor_result("rock", "scissor") == "You won, the computer chose: scissor"
    assert rock_scissor_result("rock", "paper") == "You lost, the computer chose: paper"
    assert rock_scissor_result("rock", "rock") == "It's a tie, the computer chose: rock"

    assert rock_scissor_result("paper", "scissor") == "You lost, the computer chose: scissor"
    assert rock_scissor_result("paper", "paper") == "It's a tie, the computer chose: paper"
    assert rock_scissor_result("paper", "rock") == "You won, the computer chose: rock"

    assert rock_scissor_result("scissor", "scissor") == "It's a tie, the computer chose: scissor"
    assert rock_scissor_result("scissor", "paper") == "You won, the computer chose: paper"
    assert rock_scissor_result("scissor", "rock") == "You lost, the computer chose: rock"

def test_head_tails_result():
    assert head_tails_result("heads", "heads") == "You won!!!"
    assert head_tails_result("heads", "tails") == "You lost! The coin side was tails."

    assert head_tails_result("tails", "tails") == "You won!!!"
    assert head_tails_result("tails", "heads") == "You lost! The coin side was heads."

if   __name__ =="__main__":
    main()
