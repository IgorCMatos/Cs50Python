from numb3rs import validate

def main():
    test_valid()
    test_invalid()
    test_length()

def test_valid():
    assert validate(r"0.0.0.0") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"110.135.232.23") == True

def test_invalid():
    assert validate(r"512.512.512.512") == False
    assert validate(r"55.355.83.89") == False
    assert validate(r"cat.cat.cat.cat") == False

def test_length():
    assert validate(r"0") == False
    assert validate(r"0.0") == False
    assert validate(r"0.0.0") == False
    assert validate(r"0.0.0.0") == True

if __name__ == "__main__":
    main()
