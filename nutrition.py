a = input("Item:")
b = {"Apple":"130",
     "Avocado":"50",
     "Banana":"110",
     "Cantaloupe":"50",
     "Grapefruit":"60",
     "Grapes":"90",
     "Honeydew Melon":"50",
     "Kiwifruit":"90",
     "Lemon":"15",
     "Lime":"20",
     "Nectarine":"60",
     "Orange":"80",
     "Peach":"60",
     "Pear":"100",
     "Pineapple":"50",
     "Plums":"70",
     "Strawberries":"50",
     "Sweet Cherries":"100",
     "Tangerine":"50",
     "Watermelon":"80"
     }
c = a.title()
for x in b:
    if c ==x:
        print ("Calories:",b[c])