#Summation of squares


def sum_squares(n):
    x = 0
    for i in range(1,n+1):
        x += i**2
    return x

  
n = int(input("What do you want to square? "))
print("sum of squares: ", sum_squares(n))

input("Press any ket to exit: ")

