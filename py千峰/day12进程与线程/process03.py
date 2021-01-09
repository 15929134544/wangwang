"""
多进程对于全局变量访问，在每一个全局变量里面都放一个全局变量
保证每个进程访问变量之间互不干扰
m = 1   # 不可变类型
list1 = []  # 可变类型



"""

# 进程创建
import os
from multiprocessing import Process
from time import sleep

m = 1   # 不可变类型
list1 = []  # 可变类型


def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(m)
        print('这是任务1----------', m, list1)
        # os.getppid()父进程   os.getpid()子进程


def task2(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(m)
        print('这是任务2-----------', m, list1)


# 创建进程

if __name__ == "__main__":

    # 两个开启的子进程
    p = Process(target=task1, name='任务1', args=(1, 'aa'))
    p.start()

    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p1.start()

    while True:
        sleep(1)
        m += 1
        print('-----------main', m)