def main():
    a = input("Fraction: ")
    a = str(convert(a))
    if a.isalpha():
        print (a)
    else:
        print(a+"%")
def convert(a):
    while True:
        try:
            x,y = a.split(sep="/")
            x = float(x)
            y = float(y)
            c = (x*100)/y
            if c == 100:
                c = "F"
            elif c == 0:
                c = "E"
            elif c > 100:
                c = str("Error")
            return c
        except (ValueError,ZeroDivisionError):
            print("Try again:")
main()