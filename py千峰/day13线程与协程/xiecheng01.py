# 协程：微线程
# 在有耗时操作：网络请求，网路下载（爬虫），IO操作（文件的读写），阻塞
# 协程的目的:高效利用CPU
# 进程 》线程 》协程

# Process   Thread    但是协程没有自己的类，都是通过生成器完成的
"""
生成器：yield

"""
import time


def taskA():
    for i in range(3):
        print('A'+str(i))
        yield
        time.sleep(1) # 模拟网络出现阻塞


def taskB():
    for i in range(3):
        print('B'+str(i))
        yield
        time.sleep(2) # 模拟网络出现阻塞


if __name__ == '__main__':
    # 得到一个生成器
    g1 = taskA()
    g2 = taskB()

    while True:
        try:
            next(g1)
            next(g2)
        except:
            break


