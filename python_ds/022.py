from pythonds.basic import Stack


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    # 检查是否为基本情况，即n小于进制基数。
    # 如果是，则停止递归并且从convertString中返回字符串。
    if n < base:
        return convertString[n]
    else:
        # 通过递归调用以及除法来分解问题
        return toStr(n//base, base) + convertString[n%base]


rStack = Stack()


def toStr1(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr(n//base, base)
