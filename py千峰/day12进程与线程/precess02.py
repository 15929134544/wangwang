# 进程创建
import os
from multiprocessing import Process
from time import sleep


def task1(s):
    sleep(s)
    while True:
        print('这是任务1----------', os.getpid(), '--------', os.getppid())
        # os.getppid()父进程   os.getpid()子进程


def task2(s):
    sleep(s)
    while True:
        print('这是任务2-----------', os.getpid(), '-------', os.getppid())


# 创建进程
if __name__ == "__main__":
    # print(os.getpid())
    # 两个开启的子进程
    p = Process(target=task1, name='任务1', args=(1, ))
    p.start()
    print(p.name)
    p1 = Process(target=task2, name='任务2', args=(2, ))
    p1.start()
    print(p1.name)
    print('------------')
