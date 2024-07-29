import pytest
from fuel import convert, gauge

def main():
    test_result_gauge()
    test_result_convert()
    test_result_EF()
    test_zero()
    test_input()
    test_float()

def test_result_convert():
    assert convert('3/4') == 75
    assert convert('1/4') == 25

def test_result_gauge():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"

def test_result_EF():
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_input():
    with pytest.raises(ValueError):
        convert("three/four")

def test_float():
    with pytest.raises(ValueError):
        convert("1.5/3")

if __name__ == "__main__":
    main()
