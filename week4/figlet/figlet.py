import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font = random_font)

elif len(sys.argv) == 3:
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font = sys.argv[2])

    if sys.argv[1] !="--font":
        if sys.argv[1] != "-f":
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(f"Output: {figlet.renderText(text)}")

