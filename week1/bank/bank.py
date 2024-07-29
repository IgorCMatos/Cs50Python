
def answer():

    if Greeting.startswith("hello"):
        print("$0")

    elif Greeting.startswith("h"):
        print("$20")

    else:
        print("$100")

Greeting = input("Greeting: ").strip().lower()
answer()
