"""
生产者与消费者：两个线程之间的通信

Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先进先出）队列Queue
LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原理
（可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用。
可以使用队列来实现线程间的同步

"""

"""
总结：
线程：Thread

1、创建线程：
    A:使用系统提供的Thread:t = Thread(target=func, name='', args=(), kwargs={})    新建状态
        t.start()   启动线程------》就绪状态
        run()
        t.join()让主线程让步
    B:自定义线程：
        class MyThread(Thread):
            def __init__(self, name):
                super().__init__()
                self.name = name
            
            def run(self):
                任务
        
        
        创建线程
        t = MyThread('name')
        t.start()
        
2、数据共享：
    进程共享数据与线程共享数据区别：
        进程是每个进程中都有一份
        线程共用一个数据-----》数据安全性问题
        
        因此python默认加了一个GIL
        
        GIL：全局解释器锁
        通过这个锁，我们知道线程是‘伪线程’
        
        加锁：       
        lock = Lock()
        lock.acquire()
        ...
        lock.release()
        
        -------->只要用锁：就会产生死锁
        
        避免死锁：
        1、重构代码
        2、使用timeout参数
        
3、线程间通信：生产者和消费者
    生产者：线程
    消费者：线程
    
    import queue
    
    q = queue.Queue(10)
    两个线程共用一个q对象----》通过q对象可以取值q.put()和放值q.get()
       # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()
    
    
扩展：GIL
"""

import threading
import time
import random
import queue


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put("生产者产生数据：%d" % num)
        print("生产者产生数据：%d" % num)
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到：%s' % item)
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print('END')
