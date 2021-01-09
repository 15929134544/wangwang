"""
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程
但如果是上百甚至上千个目标，手动的去创建进程的工程量巨大，此时就可以用到multiprocessing模块
提供的Pool方法。
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满。，
那么就会创建一个新的进程来执行该请求，但如果池中的进程数已经达到指定的最大值，那么
该请求就会等待，直到池中有进程结束，才会创建新的进程来执行。

在使用时分为两种类型：
1、阻塞式：添加一个执行一个，执行完一个返回一个，然后才会去添加下一个
2、非阻塞式：全部添加到队列中，然后立刻返回，并没有等待其他进程执行完毕之后才会结束，但是回调
            函数是等待任务完成之后才调用。

"""
import os
from multiprocessing import Pool
import time
from random import random


# 非阻塞式进程


def task(task_name):
    print('开始做任务啦', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    return '用时：', (end - start)


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    print('1')
    pool = Pool(5)
    print('2')
    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    print('3')
    for task1 in tasks:
        print('4')
        pool.apply_async(task, args=(task1,), callback=callback_func)  # 使用非阻塞模式
    print('5')
    pool.close()  # 添加任务结束
    print('6')
    pool.join()  #
    print('7')
    for c in container:
        print(c)

    print('------over----------')