import time


def sumOfN1(n):
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    return theSum


def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    end = time.time()
    return theSum,end - start


def sumOfN3(n):
    start = time.time()
    result = (n*(n + 1))/2
    end = time.time()
    return result,end - start


def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
        barney = bill
        fred = fred + barney
    return fred


# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN3(1000000))





