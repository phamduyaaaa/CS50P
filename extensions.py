a = input("File name: ")
b = (a.split(sep="."))
c = b[1].casefold()
if c == "gif" or c =="jpg" or c == "jpeg" or c == "png" or c =="pdf" or c =="txt" or c == "zip":
    print(f"image/{c}")
else:
    print("application/octet-stream")