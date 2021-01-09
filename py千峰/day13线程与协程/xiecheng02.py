# greenlet完成协程任务
import time

from greenlet import greenlet


def a():  # 任务A
    for i in range(5):
        print('A' + str(i))
        gb.switch()  # 切换
        time.sleep(0.1)


def b():  # 任务B
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.1)


def c():  # 任务C
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)

    ga.switch()
