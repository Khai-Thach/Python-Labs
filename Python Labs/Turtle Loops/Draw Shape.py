#Draw Shape

import turtle


a = turtle.Turtle()
a.shape("turtle")
a.color("green")
a.speed(0)

n = int(input("Enter side length: "))
             
for i in range(n):
             a.forward(50)
             a.left(360 / n)


input("Press any key to exit: ")

