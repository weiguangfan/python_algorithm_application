from turtle import *


def drawTraingle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# sierpinski首先绘制外部的三角形，接着进行3个递归调用，每一个调用对应生成的一个新三角形。
def sierpinski(points, degree, myTurtle):
    colormap = ['blue','red','green','white','yellow','violet','orange']
    drawTraingle(points, colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[1],
                    getMid(points[0],points[1]),
                    getMid(points[1],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[2],
                    getMid(points[2],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)


myTurle = Turtle()
myWin = myTurle.getscreen()
myPoints = [(-500,-250),(0,500),(500,-250)]
sierpinski(myPoints, 5, myTurle)
myWin.exitonclick()


