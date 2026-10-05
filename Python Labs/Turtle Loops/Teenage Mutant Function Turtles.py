#drawing

import turtle 

#              drawer  length of sides


bob = turtle.Turtle()
bob.shape('turtle')


#draw a square
def drawSquare(bob,side):
    for i in range(4):
        bob.fd(side)
        bob.rt(90)
        
#drawSquare(bob,50)




#draw row of squares

# turtle, # of squares in row, length of sides
def drawRow(bob,length,squareSize):
    for a in range(length):
        drawSquare(bob,squareSize)
        bob.fd(50)

#drawRow(bob, 5, 50)

bob.goto(0,0)
bob.speed(0)

#draw a grid
# turtle, x axis, y axis
def drawGrid(bob,size,squareSize):
    for a in range(5):
        drawRow(bob, size, squareSize)
        bob.rt(180)
        bob.fd(size*squareSize)
        bob.lt(90)
        bob.fd(squareSize)
        bob.lt(90)

#drawGrid(bob,5,50)



#Stair Squares        
def drawSquareStairs(bob, height, squareSize):
    for a in range(5):
        drawRow(bob,a+1, squareSize,)
        bob.lt(180)
        bob.fd((a+1)*squareSize)
        bob.lt(90)
        bob.fd(squareSize)
        bob.lt(90)


drawSquareStairs(bob,5,50)


    





