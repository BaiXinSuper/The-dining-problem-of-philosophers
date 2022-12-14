import threading  # 线程库
import time
import random


cs = [1, 1, 1, 1, 1]  # 代表5根筷子

think_time = 5  # 思考时间
eat_time = 1  # 吃饭时间
action_delay = 0


class People():
    global cs

    def __init__(self, s, e, index):
        self.left = s
        self.right = e
        self.get_l = 0
        self.get_r = 0
        self.index = index
        self.eat_time = random.randint(1, 5)
        self.think_time = random.randint(5, 10)
        self.action_delay = random.random()
        # self.eat_time=eat_time
        # self.think_time=think_time
        # self.action_delay=action_delay
        self.start()

    def start(self):
        print("\n哲学家"+self.index+"准备抢夺筷子"+str(self.left))
        while not self.get_l:
            if cs[self.left]:
                cs[self.left] = 0
                self.get_l = 1
                time.sleep(self.action_delay)
                print("\n哲学家"+self.index+"抢夺了筷子"+str(self.left))
        # time.sleep(self.action_delay)
        while self.get_l and not self.get_r:
            if cs[self.right]:
                cs[self.right] = 0
                self.get_r = 1
                time.sleep(self.action_delay)
                print("\n哲学家"+self.index+"抢夺了筷子"+str(self.right))

        self.eat()

    def eat(self):
        if self.get_l and self.get_r:
            print("\n哲学家"+self.index+"已经吃上饭了")
            time.sleep(self.eat_time)
            print("\n哲学家"+self.index+"吃完饭了并且开始思考")
            self.get_l = 0
            self.get_r = 0
            cs[self.left] = 1
            cs[self.right] = 1
            # time.sleep(self.action_delay)
            self.think()

    def think(self):
        time.sleep(self.think_time)
        print("\n哲学家"+self.index+"思考结束，准备吃饭")
        # time.sleep(self.action_delay)
        self.start()


def main():
    tA = threading.Thread(target=lambda: People(0, 1, "A"))
    tB = threading.Thread(target=lambda: People(1, 2, "B"))
    tC = threading.Thread(target=lambda: People(2, 3, "C"))
    tD = threading.Thread(target=lambda: People(3, 4, "D"))
    tE = threading.Thread(target=lambda: People(4, 0, "E"))
    tA.start()
    tB.start()
    tC.start()
    tD.start()
    tE.start()


main()
