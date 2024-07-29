import pytest
from working import convert

def main():
    test_right()
    test_hour()
    test_minute()
    test_format()

def test_right():
    assert convert("8 AM to 11 AM") == "08:00 to 11:00"
    assert convert("4 PM to 7:25 PM") == "16:00 to 19:25"
    assert convert("8:35 PM to 5 AM") == "20:35 to 05:00"
    assert convert("5 AM to 11 PM") == "05:00 to 23:00"

def test_hour():
    with pytest.raises(ValueError):
        convert("15 AM to 18 PM")
    with pytest.raises(ValueError):
        convert("27 PM to 16 AM")

def test_minute():
    with pytest.raises(ValueError):
        convert("8:75 AM to 22:123 PM")
    with pytest.raises(ValueError):
        convert("22:86 PM to 04:90 AM")

def test_format():
    with pytest.raises(ValueError):
        convert("5 AM = 7PM")
    with pytest.raises(ValueError):
        convert("2 AM go 7PM")

if __name__ == "__main__":
    main()
