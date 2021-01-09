"""
单核CPU实现多任务的原理：操作系统轮流让各个任务交替执行

多核CPU实现多任务原理：真正的秉性执行多任务只能在多核CPU上执行，但是由于任务数量远远多于CPU的
核心数量，所以，操作系统也会自动把很多任务轮流调度到很多核心上执行

——并发和并行：
    并发：当有多个线程在操作时，如果系统只有一个CPU，那么它根本不可能同时进行一个以上的多个
    线程，它只能把CPU的运行时间划分为多个时间段，再将时间段分配给各个线程执行，在一个时间段
    的线程代码执行时，其他线程处于挂起状态。这种方式我们称之为并发（Concurrent）


    并行：当系统有一个以上的CPU时，则线程的操作有可能非并发，当一个CPU执行一个线程时，另一个
    CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，这种方式称之为并行（Parallel）

    实现多任务的方式：
    -多进程模式
    -多线程模式
    -协程

    关系：进程 》 线程 》协程

    多进程：
    进程（Process）是系统进行资源分配和调度的基本单位
    进程是线程的容器。程序是指令、数据及其组织形式的描述，进程是程序的实体。

    对于操作系统来说，一个任务就是一个进程

    优点：
        稳定性高，一个进程崩溃了，不会影响其他进程（进程之间互相独立）

    缺点：
        创建进程开销巨大
        操作系统可以同时运行的进程数目有限


    创建进程：
    1、导入：from multiprocessing import Process
    2、创建进程：process = Process(target=函数，name=进程的名字，args=（给函数传递的参数）)
                process对象

    3、对象调用方法
    process.start() 启动进程并执行任务
    process.run()   只是执行了这个任务，但是没有启动进程
    terminate()     终止进程
"""

# 进程创建
import os
from multiprocessing import Process
from time import sleep


def task1():

    while True:
        sleep(1)
        print('这是任务1----------', os.getpid(), '--------', os.getppid())
        # os.getppid()父进程   os.getpid()子进程


def task2():

    while True:
        sleep(2)
        print('这是任务2-----------', os.getpid(), '-------', os.getppid())


# 创建进程
number = 1

if __name__ == "__main__":
    print(os.getpid())
    # 两个开启的子进程
    p = Process(target=task1, name='任务1')
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2')
    p1.start()
    print(p1.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p.terminate()
            p1.terminate()
            break
        else:
            print('--------------', number)

    print('------------')