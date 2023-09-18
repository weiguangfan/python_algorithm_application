from turtle import *

# 先导入turtle模块，然后创建一个小乌龟对象，同时也会创建用于绘制图案的窗口。
myTurtle = Turtle()
myWin = myTurtle.getscreen()


def drawSpiral(myTurtle, lineLen):
    # 基本情况是，要画的线的长度（参数len）降为0。
    if lineLen >0:
        # 如果线的长度大于0，就让小乌龟向前移动len个单位距离，然后向右转90度。
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        # 递归发生在用缩短后的距离再一次调用drawSpiral函数时。
        drawSpiral(myTurtle, lineLen-5)


drawSpiral(myTurtle, 100)
# 调用了myWin.exitonclick()函数，这使小乌龟进入等待模式，直到用户在窗口内再次点击之后，程序清理并退出。
myWin.exitonclick()






