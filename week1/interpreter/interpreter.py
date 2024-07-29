num = input("Expression: ")
x, y, z = num.split(" ")
x = float(x)
z = float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

result = round(result, 1)
print (result)
