class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        # 队列的尾部在列表的位置0处
        self.items.insert(0,item)

    def dequeue(self):
        # pop则可用于移除队列头部的元素（列表中的最后一个元素）
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue('dog')
    q.enqueue(4)
    print(q.isEmpty())
    q.enqueue(True)
    print(q.size())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())