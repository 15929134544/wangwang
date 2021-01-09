# 阻塞式
"""
特点：
添加一个执行一个任务，如果一个任务不结束，另一个任务就进不来。

"""

from multiprocessing import Pool
import time
from random import random


# 阻塞式进程


def task(task_name):
    print('开始做任务啦', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print('用时：', (end - start))

#
# container = []
#
#
# def callback_func(n):
#     container.append(n)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply(task, args=(task1,))  # 使用非阻塞模式

    pool.close()
    pool.join()

    print('------over---------')

"""
总结：

进程池：
1、创建进程池对象：pool = Pool(最大值)
2、向进程池加东西：有两种方式：
    ———阻塞式：pool.apply()
    ———非阻塞式：pool.apply_async()
    
    pool.close()    停止添加进程
    pool.join()     让主进程让步
"""