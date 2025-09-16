#TurtleGraphics.py
#Name: Tucker Quinn
#Date: September 15th, 2025
#Assignment: Turtle Graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size): # draws a square of a chosen width
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon (myTurtle, sides): # draws a polygon with a chosen number of sides
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)
        
def fillCorner (myTurtle, corner): # draws a square of width 100 and fills a chosen corner
    drawSquare (myTurtle, 100)
    if (corner == 1):
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    if (corner == 2):
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    if (corner == 3):
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    if (corner == 4):
        myTurtle.up()
        myTurtle.forward(50)
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
def squaresInSquares (myTurtle, num): # draws a chosen number of concentric squares
    length = 25
    for i in range(num):
        drawSquare(myTurtle, length)
        length = length + 25
        myTurtle.up()
        myTurtle.left(135)
        myTurtle.forward(0.7071067812*25)
        myTurtle.right(135)
        myTurtle.down()
        
def main():
    myTurtle = turtle.Turtle()
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
