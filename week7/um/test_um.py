from um import count

def main():
    test_lower()
    test_upper()
    test_zero()
    test_wrong()

def test_lower():
    assert count("um") == 1
    assert count("um, thanks, um.") == 2

def test_upper():
    assert count("Um") == 1
    assert count("Um, thanks, um.") == 2

def test_zero():
    assert count("thanks") == 0

def test_wrong():
    assert count ("Umwau") == 0
    assert count ("Umwau, um") == 1

if __name__ == "__main__":
    main()
