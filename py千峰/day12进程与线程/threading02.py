import threading
"""
线程是可以共享全局变量的-----》数据不安全

GIL:全局解释器锁  保证数据的安全性
缺点：速度慢

python底层只要用线程，就会默认加锁

线程：耗时操作、爬虫、IO操作
进程；计算密集型

"""

money = 1000


def run1():
    global money
    for i in range(100):
        money -= 1


def run2():
    global money
    for i in range(100):
        money -= 1


if __name__ == '__main__':
    # 创建线程
    th1 = threading.Thread(target=run1, name='th1')
    th2 = threading.Thread(target=run2, name='th2')

    # 启动线程
    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print('money:', money)