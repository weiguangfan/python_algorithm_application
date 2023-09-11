from pythonds.basic import Stack


def postfixEval(postfixExpr):
    # 保存操作数
    operandStack = Stack()
    # 将输入的后序表达式转换成一个列表
    tokenList = postfixExpr.split()
    for token in tokenList:
        # 如果标记是操作数，将其转换成整数并且压入operandStack栈中。
        if token in '0123456789':
            operandStack.push(int(token))
        # 如果标记是运算符，从operandStack栈中取出两个操作数。
        # 第一次取出右操作数，第二次取出左操作数。
        # 进行相应的算术运算，然后将运算结果压入operandStack栈中。
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    # 当处理完输入表达式时，栈中的值就是结果。将其从栈中返回。
    return operandStack.pop()


def doMath(op,op1,op2):
    if op == "*":
       return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2








