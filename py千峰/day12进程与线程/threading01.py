# 线程
"""
    考虑？创建线程？如何使用线程？

线程状态：
    新建状态-----start----->就绪状态---CPU调用（进入CPU）--->运行状态-------->结束状态
                                                            |
                                                      sleep |
                                                        阻塞状态（睡醒之后进入就绪状态）

    创建线程：t = threading.Thread(target=download, name='aa', args=(1, ))
    使用线程：t.start()

    线程状态：
    新建  就绪  运行  阻塞  结束




"""
import threading

# 进程：Process
# 线程：Thread
from time import sleep


def download(m):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载', image)
        sleep(m)
        print('下载成功'.format(image))


def listenMusic():
    musics = ['大碗宽面', '烤面筋', '土耳其冰淇淋', '烤馒头片']
    for music in musics:
        sleep(0.5)
        print('正在听{}'.format(music))


if __name__ == '__main__':

    # 线程对象
    t = threading.Thread(target=download, name='aa', args=(1, ))
    # 启动线程
    t.start()

    t1 = threading.Thread(target=listenMusic, name='bb')
    t1.start()

    n = 1
    while True:
        sleep(1.5)
        print(n)
        n += 1