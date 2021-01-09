# 括号里放的是可以通过import导入并可以使用的内容
__all__ = ['add', 'number', 'Calculate']
# 变量
number = 100
name = 'calculation'


# 函数


def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum

    else:
        print('至少传入两个参数')
        return 0


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m

    else:
        print('至少传入两个参数')
        return 0


def multiply(*args):
    pass


def divide(*args):
    pass


# 类
class Calculate:

    def __init__(self, num):
        self.num = num

    def test(self):
        print('正在使用calculate进行计算')

    @classmethod
    def test1(cls):
        print('------Calculate中的类方法')


def test():
    print('我是测试')


# 如果希望函数调用不执行
print('---name------', __name__)  # __main__

if __name__ == '__main__':
    print(__name__)  # __main__
    test()
