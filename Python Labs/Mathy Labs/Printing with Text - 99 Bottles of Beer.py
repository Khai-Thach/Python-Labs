#Printing with Text: 99 Bottles of Beer

def bottles(a):
    for i in range(a):
        print(a-i, "bottles of beer on the wall,", a-i, "bottles of beer")
        print("Take one down, pass it around,", a-i-1, "bottles of beer on the wall")

beers = int(input("How many bottles of beer do you want? "))
bottles(beers)

input("Press any key to exit: ")
