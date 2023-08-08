def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = 0
    if 2<=len(s)<=6 and s[:2].isalpha() and s.isalnum() and s[2] != "0":
        for x in s:
            if x.isdigit():
                index = s.index(x)
                if s[index:].isdigit():
                    return True
    else:
        return False
main()