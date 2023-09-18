def moveDisk(fp, tp):
    print("moving disk from %d to %d\n" % (fp, tp))


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        # 将除了最后一个盘子以外的其他所有盘子从起点柱子移到中间柱子。
        moveTower(height - 1, fromPole, withPole, toPole)
        # 说明将盘子从一根柱子移到另一根柱子。
        # 将最后一个盘子移到终点柱子。
        moveDisk(fromPole, toPole)
        # 将之前的塔从中间柱子移到终点柱子，并将其放置在最大的盘子之上。
        moveTower(height - 1, withPole, toPole, fromPole)














