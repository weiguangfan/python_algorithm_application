from turtle import *

t = Turtle()
myWin = t.getscreen()


def tree(branchLen, t):
    # if语句会检查branchLen是否满足基本情况。
    if branchLen > 5:
        # 让它向前。
        t.forward(branchLen)
        # 在小乌龟向右转了20度之后立刻进行递归调用，这就是之前提到的右子树。
        # 然后，再一次进行递归调用，但这次是在向左转了40度以后。
        # 之所以需要让小乌龟左转40度，是因为它首先需要抵消之前右转的20度，然后再继续左转20度来绘制左子树。
        t.right(20)
        # 每一次进行递归调用时，都从参数branchLen中减去一些，这是为了让递归树越来越小。
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        # 让它向后
        t.backward(branchLen)


if __name__ == "__main__":
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color('green')
    tree(110, t)
    myWin.exitonclick()