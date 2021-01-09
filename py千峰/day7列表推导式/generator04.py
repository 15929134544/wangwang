# 进程 > 线程 > 协程
# 通过携程可以使任务交替执行
# 迅雷：


def task1(n):
    for i in range(n):
        print('正在搬第{}块砖'.format(i))
        yield None


def task2(n):
    for i in range(n):
        print('正在听第{}首歌'.format(i))
        yield None


# 想让任务交替执行


g1 = task1(10)
g2 = task2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break


"""
生成器：generator

定义方式：
1、通过列表推导式
g = (x+1 for x in range(6))
2、借助于函数和yield
def func():
    ...
    yield
    
g = func() 此时的g就是一个生成器


产生元素：
1、next(generator)--------->每调用一次都会产生一个新元素，
如果元素产生完毕，再次调用就会产生异常
2、生成器自己的方法：
    g.__next__()
    g.send(value)   
    
    
生成器应用：协程
"""
