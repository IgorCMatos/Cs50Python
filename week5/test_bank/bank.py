def main():

    Greeting = input("Greeting: ").strip().lower()
    Greeting_value = value(Greeting)
    print(f"${Greeting_value}")

def value(Greeting):

    if Greeting.startswith("hello"):
        return 0
    elif Greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


