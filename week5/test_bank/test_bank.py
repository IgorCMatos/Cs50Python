from bank import value

def main():
    print()


def test_value_else():
    assert value("what are you doing?") == 100
    assert value("Good Night") == 100
    assert value("It's good to see you") == 100

def test_value_hello():
    assert value("hello") == 0
    assert value("hello my friend") == 0
    assert value("Hello, Cs50") == 0

def test_value_h():
    assert value("how are you?") == 20
    assert value("hey, friend") == 20
    assert value("hey you") == 20



if __name__ == "__main__":
    main()
