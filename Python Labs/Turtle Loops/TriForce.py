import turtle

inner = turtle.Turtle()

for i in range(3):
    inner.forward(100)
    inner.right(120)

outer = turtle.Turtle()

outer.left(60)
outer.forward(100)


for i in range (3):
    outer.right(120)
    outer.forward(200)

input("Press any key to exit: ")
