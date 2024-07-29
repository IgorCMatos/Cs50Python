
coke_price = 50
accepted_coins = [5, 10, 25]

while coke_price > 0:

    print(f"Amount Due: {coke_price}")
    coin = int(input("Insert Coin: "))

    if coin in accepted_coins:
        coke_price -= coin

    else:
        print("Invalid coin. Please use 5, 10, or 25 cents coins.")

if coke_price <= 0:
    change = coke_price * -1
    print(f"Change Owed: {change}")


