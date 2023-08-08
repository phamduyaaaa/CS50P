def main():
    a = input("What time is it? ")
    check = convert(a)
    if 7<check<8:
        print("breakfast time")
    elif 12<check<13:
        print("lunch time")
    elif 18<check<19:
        print("dinner time")
def convert(time):
    a,b = time.split(sep = ":")
    a = float(a)
    b = float(b)
    return a+(b/60)
if __name__ == "__main__":
    main()