a = input()
x, y, z = a.split(sep = " ")
x = float(x)
z = float(z)
if y == "+":
    c = x + z
elif y == "-":
    c = x - z
elif y == "*":
    c = x * z
elif y == "/":
    c = x / z
elif y == "%":
    c = x % z
print(c)

