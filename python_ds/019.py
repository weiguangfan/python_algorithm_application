class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        # 列表中的每一个元素都必须被存放在一个节点对象中。
        # 创建一个新节点，并且将元素作为其数据。
        # 现在需要将新节点与已有的链表结构链接起来。
        temp = Node(item)
        # 将新节点的next引用指向当前列表中的第一个节点。
        # 这样一来，原来的列表就和新节点正确地链接在了一起。
        temp.setNext(self.head)
        # 修改列表的头节点，使其指向新创建的节点。
        self.head = temp

    def length(self):
        # current就是外部引用，它被初始化为列表的头节点。
        current = self.head
        # 在计算开始时，由于没有访问到任何节点，因此count被初始化为0。
        count = 0
        # 只要current引用没有指向列表的结尾（None），就将它指向下一个节点
        while current != None:
            # 每当current指向一个新节点时，将count加1。
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        # 遍历从列表的头部开始
        current = self.head
        # 使用布尔型变量found来标记是否找到所需的元素。
        # 由于一开始时并未找到该元素，因此将found初始化为False。
        found = False
        # 既考虑了是否到达列表末尾，也考虑了是否已经找到目标元素。
        while current != None and not found:
            # 检查当前节点中的元素是否为目标元素。如果是，就将found设为True。
            if current.getData() == item:
                found = True
            else:
                # 检查当前节点中的元素是否为目标元素。如果是，就将found设为True。
                current = current.getNext()
        return found

    def remove(self, item):
        # 对两个引用进行初始赋值。
        # 从列表的头节点开始。
        current = self.head
        # 由于头节点之前没有别的节点，因此previous的初始值是None
        previous = None
        # 布尔型变量found再一次被用来控制循环。
        found = False
        while not found:
            # 检查当前节点中的元素是否为要移除的元素。
            # 如果是，就设found为True。
            if current.getData() == item:
                found = True

            else:
                # 如果否，则将previous和current往前移动一次。
                # 这两条语句的顺序十分重要。
                # 必须先将previous移动到current的位置，然后再移动current。
                # 这一过程经常被称为“蠕动”，因为previous必须在current向前移动之前指向其当前位置。
                previous = current
                current = current.getNext()
        # 如果被移除的元素正好是链表的第一个元素，那么current会指向链表中的第一个节点，previous的值则是None。
        # 在这种情况下，需要修改链表的头节点，而不是previous指向的节点
        if previous == None:
            # 链表的头节点被修改成指向当前头节点的下一个节点，从而达到移除头节点的效果。
            self.head = current.getNext()
        else:
            # 一旦搜索过程结束，就需要执行移除操作。
            # 如果previous的值不是None，则说明需要移除的节点在链表结构中的某个位置。
            # 在这种情况下，previous指向了next引用需要被修改的节点。
            # 使用previous的setNext方法来完成移除操作。
            previous.setNext(current.getNext())

