from seasons import valid_date , valid_date

def main():
    test_valid_date()
    test_invalid_date()

def test_valid_date():
    assert valid_date("1999-01-01") == ('1999','01','01')

def test_invalid_date():
    assert valid_date("January 1, 1999") == None
    assert valid_date("1-1-1") == None

if __name__ == "__main__":
    main()
