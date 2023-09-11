from pythonds.basic import Stack
import string


def infixToPostfix(infixexpr):
    # 保存运算符的优先级值
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    # 用于保存运算符
    opStack = Stack()
    # 用于保存结果
    postfixList = []
    # 将输入的中序表达式转换成一个列表
    tokenList = infixexpr.split()

    for token in tokenList:
        # 如果标记是操作数，将其添加到结果列表的末尾。
        if token in string.ascii_uppercase:
            postfixList.append(token)
        # 如果标记是左括号，将其压入opstack栈中。
        elif token == '(':
            opStack.push(token)
        # 如果标记是右括号，反复从opstack栈中移除元素，直到移除对应的左括号。
        # 将从栈中取出的每一个运算符都添加到结果列表的末尾。
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        # 如果标记是运算符，将其压入opstack栈中。
        # 但是，在这之前，需要先从栈中取出优先级更高或相同的运算符，并将它们添加到结果列表的末尾。
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    # 当处理完输入表达式以后，检查opstack。
    # 将其中所有残留的运算符全部添加到结果列表的末尾。
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


if __name__ == "__main__":
    print(infixToPostfix("( A + B ) * ( C + D )"))
    print(infixToPostfix(" ( A + B) * C"))
    print(infixToPostfix(" A + B * C"))







