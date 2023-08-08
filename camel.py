a = input("camelCase: ")
b = "_"
print ("snake_case: ",end="")
for i in a:
    if i == i.upper():
        i = b + i.lower()
    print(i,end ="" )