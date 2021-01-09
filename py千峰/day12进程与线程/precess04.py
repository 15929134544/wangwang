# 自定义进程
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            # print('进程名字：'+self.name)
            print('{}---------->自定义进程,{}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
    p = MyProcess('小明')
    p.start()

    p1 = MyProcess('小红')
    p1.start()
