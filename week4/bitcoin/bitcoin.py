import requests
import sys

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    else:
        Quantity = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    Link = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    Bitcoin_price  = Link["bpi"]["USD"]["rate_float"]

    Bitcoin_final = Bitcoin_price * Quantity
    print(f"${Bitcoin_final:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)
