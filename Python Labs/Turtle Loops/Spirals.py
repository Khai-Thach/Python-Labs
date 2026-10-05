# Spirals

#N Sided Polygon

import turtle

bob=turtle.Turtle()
bob.shape('turtle')
bob.speed(0)


def drawNgon(bob, numSides, sideLength):
    for i in range(numSides):
        bob.fd(sideLength)
        bob.rt(360/numSides)




#drawNgon(bob,6,100)


#Super Spiral


#turtle, defines shape, size of each polygon, number of polygons 
def drawNgonSpiral(bob, numSides, sideLength, numShapes):
    for a in range(numShapes):
        drawNgon(bob,numSides,sideLength)
        bob.rt(20.57)



drawNgonSpiral(bob,6,100,35)
    
