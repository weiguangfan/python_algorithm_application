from pythonds.basic import Stack


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    # 检查是否为基本情况，即n小于进制基数。
    # 如果是，则停止递归并且从convertString中返回字符串。
    if n < base:
        return convertString[n]
    else:
        # 通过递归调用以及除法来分解问题
        return toStr(n//base, base) + convertString[n % base]


rStack = Stack()


def toStr1(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        # 不拼接递归调用toStr的结果和convertString的查找结果，而是在进行递归调用之前把字符串压入栈中。
        # 只需执行出栈操作和拼接操作，就能得到最终结果
        rStack.push(convertString[n % base])
        toStr(n//base, base)


if __name__ == '__main__':
    print(toStr(769, 10))
    print(toStr(10, 2))


