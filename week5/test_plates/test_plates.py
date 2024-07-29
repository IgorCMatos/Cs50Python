from plates import is_valid

def main():
    test_length()
    test_start_letters()
    test_numbers_middle()
    test_zero_first()
    test_punctuation_spaces()

def test_length():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CSPython") == False
    assert is_valid("Python") == True

def test_start_letters():
    assert is_valid("PY") == True
    assert is_valid("50") == False

def test_numbers_middle():
    assert is_valid("CS50py") == False
    assert is_valid("CS50") == True

def test_zero_first():
    assert is_valid("CS050") == False

def test_punctuation_spaces():
    assert is_valid("CS!!50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS'50") == False


if __name__ == "__main__":
    main()
