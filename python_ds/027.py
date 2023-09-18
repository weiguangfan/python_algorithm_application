from turtle import *


class Maze:
    def __init__(self, mazeFileName):
        # 行数
        rowsInMaze = 0
        #
        columnsInMaze = 0
        # 存储文件每一行的符号集合
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        # 遍历文件的每一行
        for line in mazeFile:
            # 存储每一行的符号
            rowList = []
            # 用于计数
            col = 0
            # 遍历每一行的每个符号
            for ch in line[:-1]:
                # 将每个字符添加到列表
                rowList.append(ch)
                # 特殊符号判断
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                # 叠加
                col = col + 1
            # 记录行数
            rowsInMaze = rowsInMaze + 1
            # 将每一行的符号添加进列表
            self.mazelist.append(rowList)
            # 最后一行的符号数量
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        setup(width=600, height=600)
        setworldcoordinates(-(columnsInMaze - 1)/2 - .5,
                            -(rowsInMaze - 1)/2 - .5,
                            (columnsInMaze - 1)/2 + .5,
                            (rowsInMaze - 1)/2 + .5
                            )








def searchFrom(maze, startRow, startColumn):
    maze.updatePostion(startRow, startColumn)
    # 检查基本情况
    # 1. 遇到墙
    if maze[startRow][startColumn] == OBSTACLE:
        return False
