
def Results():

    if percentage_fuel >= 99:
        print("F")
    elif percentage_fuel <= 1:
        print("E")
    else:
        print(f"{percentage_fuel}%")

while True:
    try:

        fuel = input("Fraction: ")

        x, y = fuel.split("/")
        x = int(x)
        y = int(y)

        fuel_fraction  = x / y
        percentage_fuel = fuel_fraction * 100
        percentage_fuel = round(percentage_fuel)

        if fuel_fraction <= 1:
            break

    except(ValueError):
        print("The value is invalid for the given operation")
    except(ZeroDivisionError):
        print("Division by zero is not allowed in mathematics")

Results()
