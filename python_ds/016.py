import random
from pythonds.basic import Queue


class Printer:
    """检查当前是否有待完成的任务。"""
    def __init__(self, ppm):
        # 其构造方法会初始化打印速度，即每分钟打印多少页。
        self.pagerate = ppm
        # 是否有待完成的任务
        self.currentTask = None
        # 工作所需的时间
        self.timeRemaining = 0

    def tick(self):
        """
        tick方法会减量计时，并且在执行完任务之后将打印机设置成空闲状态"""
        if self.currentTask != None:
            # 打印机进行一秒的打印，同时从该任务的执行时间中减去一秒。
            self.timeRemaining = self.timeRemaining - 1
            # 如果打印任务执行完毕，或者说任务需要的时间减为0，则说明打印机回到空闲状态。
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        """如果有，那么打印机就处于工作状态"""
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        # 并且其工作所需的时间可以通过要打印的页数来计算。
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


class Task:
    """打印任务队列"""
    def __init__(self, time):
        # 每一个任务都需要保存一个时间戳，用于计算等待时间。
        # 这个时间戳代表任务被创建并放入打印任务队列的时间。
        self.timestamp = time
        # 当任务被创建时，随机数生成器会随机提供页数，取值范围是1~20。
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        """waitTime方法可以获得任务在队列中等待的时间。"""
        return currenttime - self.timestamp


def newPrintTask():
    """可以通过1~180的一个随机数来模拟每秒内产生打印任务的概率。
    布尔辅助函数newPrintTask判断是否有新创建的打印任务。
    我们再一次使用random模块中的randrange函数来生成随机数，不过这一次的取值范围是1~180。
    平均每180秒有一个打印任务。
    通过从随机数中选取180，可以模拟这个随机事件。"""
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    """

    :param numSeconds: 总时间
    :param pagesPerMinute:打印机每分钟打印多少页
    :return:
    """
    labprinter = Printer(pagesPerMinute)
    # printQueue对象是队列抽象数据类型的实例。
    # 创建一个打印任务队列。
    # 每一个任务到来时都会有一个时间戳。
    # 一开始，队列是空的。
    printQueue = Queue()
    # 存放任务的等待时间的一个列表
    waitingtimes = []
    # 针对每一秒（currentSecond），执行以下操作。
    for currentSecond in range(numSeconds):
        # 打印任务发生，就添加到打印任务队列
        # 是否有新创建的打印任务？
        # 如果是，以currentSecond作为其时间戳并将该任务加入到队列中。
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        # 打印机空闲，并且打印任务队列不为空
        # 如果打印机空闲，并且有正在等待执行的任务，执行以下操作：
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # 取出打印任务
            # 从队列中取出第一个任务并提交给打印机；
            nexttask = printQueue.dequeue()
            # 计算等待时间：开始执行打印任务时间减去打印任务添加时间
            # 用currentSecond减去该任务的时间戳，以此计算其等待时间；
            # 将该任务的等待时间存入一个列表，以备后用；
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # 计算打印时间
            # 根据该任务的页数，计算执行时间。
            labprinter.startNext(nexttask)
        # 打印机进行一秒的打印，同时从该任务的执行时间中减去一秒。
        labprinter.tick()
    # 当模拟完成之后，根据等待时间列表中的值计算平均等待时间。
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print(" Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 5)






