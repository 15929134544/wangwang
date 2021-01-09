# 进程间的通信
from multiprocessing import Process, Queue
from socket import timeout
from time import sleep


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载', image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}文件保存成功'.format(file))
        except:
            print('全部保存完毕')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))

    p2 = Process(target=getfile, args=(q,))

    # 启动进程
    p1.start()
    p1.join()

    p2.start()
    p2.join()
"""
线程是依赖于进程的，线程之间并发执行
多线程：（multithreading）
优点：使用线程可以把占据长时间的程序中的任务放到后台去处理
程序运行速度可以加快

"""