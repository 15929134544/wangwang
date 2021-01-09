"""
又想并行执行线程，又想保证数据的安全性，则引入同步

如果多个线程共同对某个数据进行修改，则可能出现不可预料的后果，为了保证数据的正确性，需要对
多个线程，需要对多个线程进行同步。
同步：一个一个的完成，一个完成另一个才能进来。效率就会降低。

使用Thread对象的Lock或者Rlock可以实现简单的线程同步，这两个对象都有acquire和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其放在acquire和release方法之间。（就可以将
要操作的数据锁住）

多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在
数据不同步的问题，为了避免这种情况，所以才引入了锁的概念。

使用锁步骤：
1、创建锁对象：lock = threading.Lock()

2、请求得到锁：lock.acquire()
    进行数据共享的操作...
3、释放锁：lock.release()

只要不释放锁，其他的线程都无法进入运行状态。

"""

import threading
import random
import time

# 创建锁对象
lock = threading.Lock()

list1 = [0] * 10  # 列表可以用+/*，*表示10个0


def task1():
    # 申请获取线程锁,如果已经上锁，则等待锁的释放
    # lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)

    # lock.release()


def task2():
    # lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print('--------->', list1[i])
        time.sleep(0.5)

    # lock.release()


if __name__ == '__main__':
    # 创建线程
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t2.start()
    t1.start()

    t2.join()
    t1.join()

    print(list1)
