print("Amount Due:", 50)
c = 0
b = 50
while (c != 50):
    a = int(input("Insert Coin: "))
    if a == 25 or a == 10 or a == 5:
        b -= a
        print("Amount Due:", b)
        c += a
    else:
        print("Amount Due:", b)
        continue
print("Change Owed:",0)