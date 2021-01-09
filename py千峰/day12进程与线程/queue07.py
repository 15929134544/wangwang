# 进程间通信
# 队列
from multiprocessing import Queue

q = Queue(5)

# 向队列里面放东西
q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())

# 放值（判断队列是否为满）
if not q.full():  # full用来判断队列是否满了    q.empty（）判断队列是否是空
    q.put('F', timeout=3, )  # 如果队列满了，则只能等待，除非有’空地‘，则添加成功
    # timeout=3表示等待3秒之后，没有空位，则报异常
else:
    print('队列已满')

# 取值（判断队列是否为空）
if not q.empty():
    q.get()
else:
    print('')

# 不阻塞
# q.put_nowait()
# q.get_nowait()
