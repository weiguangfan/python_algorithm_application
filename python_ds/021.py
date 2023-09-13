

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


def listsum1(numList):
    # 检查列表是否只包含一个元素。
    # 这个检查非常重要，同时也是该函数的退出语句。
    # 对于长度为1的列表，其元素之和就是列表中的数。
    if len(numList) == 1:
        return numList[0]
    else:
        # listsum函数调用了自己！
        # 这就是我们将listsum称为递归函数的原因——递归函数会调用自己。
        return numList[0] + listsum1(numList[1:])


