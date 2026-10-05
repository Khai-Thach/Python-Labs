#Printing with Text: Multiplication Table

def table(n):
    for a in range (1,n+1):
        for b in range(1,n+1):
            print(a*b, end= ' ')
        print('\t')
multiplication = int(input("What do you want to mutiply? "))
table(multiplication)

input("Press any ket to exit: ")

