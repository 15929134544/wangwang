# 魔术方法:与普通方法不同，普通方法需要调用，而魔术方法是在特定时刻自动触发
"""
__init__：初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）

__new__:实例化的魔术方法
触发时机：在实例化时触发

__call__:调用对象时的魔术方法
触发时机：将对象当作函数调用时触发   对象()

"""


class Person:
    def __init__(self, name):
        self.name = name
        print('--------init', self)  # <__main__.Person object at 0x02C70270>

    def __new__(cls, *args, **kwargs):  # __new__:向内存申请地址
        print('---------new')
        position = object.__new__(cls)  # 地址
        print(position)  # <__main__.Person object at 0x02C70270>
        return position

    # 表示调用
    def __call__(self, name):
        print('-----------call', name)


p = Person('jack')

print(p)    # <__main__.Person object at 0x02C70270>

# 如果想把对象当作函数调用时，需要重写__call__
p('hello')  # hello


"""
总结：
__new__()：负责开辟空间，将地址return回给self
__init__():init拿到地址，进行初始化
初始化之后，将地址传给对象
"""
