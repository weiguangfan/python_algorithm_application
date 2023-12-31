import timeit
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [1]
    # return l


def test2():
    l = []
    for i in range(1000):
        l.append(i)
    # return l


def test3():
    l = [i for i in range(1000)]
    # return l


def test4():
    l = list(range(1000))
    # return l


if __name__ == '__main__':
    # print(timeit.timeit('test1()', setup='from __main__ import test1'))
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer("test2()","from __main__ import test2")
    print("concat ", t2.timeit(number=1000), "milliseconds")

    t3 = Timer("test3()","from __main__ import test3")
    print("concat ", t3.timeit(number=1000), "milliseconds")

    t4 = Timer("test4()","from __main__ import test4")
    print("concat ", t4.timeit(number=1000), "milliseconds")





