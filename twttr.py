a = input("Input: ")
for x in a:
    if x.lower() == "a" or x.lower() == "e" or x.lower() == "i" or x.lower() == "o" or x.lower() == "u":
        a = a.replace(x,"")
print("Output:",a)