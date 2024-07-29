from twttr import shorten

def main():
    test_uplower_cases()
    test_number_cases()
    test_special_cases()

def test_uplower_cases():

    assert shorten("TWitTer") == "TWtTr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"

def test_number_cases():
     assert shorten("Twitter 123") == "Twttr 123"
     assert shorten("123 twitter") == "123 twttr"

def test_special_cases():
    assert shorten("What's your Twitter?") == "Wht's yr Twttr?"

if   __name__ =="__main__":
    main()
