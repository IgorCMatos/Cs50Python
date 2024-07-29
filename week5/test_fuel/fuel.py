
def main():
    fraction = input("Fraction: ")
    fuel_fraction = convert(fraction)
    result = gauge(fuel_fraction)
    print (result)

def convert(fraction):

    while True:

        try:

            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            fraction  = x / y

            if fraction <= 1:
                percentage_fuel = round(fraction * 100)
                return percentage_fuel
            else:
                 fraction = input("Fraction: ")
                 pass

        except(ValueError):
            print("The value is invalid for the given operation")
            raise
        except(ZeroDivisionError):
            print("Division by zero is not allowed in mathematics")
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
