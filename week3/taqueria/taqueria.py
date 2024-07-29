
Food_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

Total_price = 0

while True:
    try:

        item = input("Item: ").title()

        if item in Food_prices:
            Total_price += Food_prices[item]
            print(f"Total: ${Total_price:.2f}")

    except EOFError:
        print()
        break

