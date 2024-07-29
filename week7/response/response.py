from validator_collection import validators

def main():

    email = input("What's your email address? ").strip()
    is_valid(email)

def is_valid(email):
        try:
              validators.email(email)
              print("Valid")

        except:
              print("Invalid")

if __name__ == "__main__":
      main()
