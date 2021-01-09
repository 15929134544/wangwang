"""
__del__:delete的缩写   析构魔术方法
触发时机：当对象没有用（没有任何变量引用）的时候被触发

1、对象赋值：
    p = Person()
    p1 = p
    说明p和p1共同指向同一个地址
2、删除地址的引用
    del p1  删除p1对地址的引用

3、查看对地址的引用的次数
    import sys
    sys.getrefcount(p)

4、当一块空间没有了任何引用，默认执行__del__


"""

import sys


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('-------del----------')


p = Person('jack')

# 对象赋值
p1 = p
print(p1.name)

p1.name = 'tom'
print(p.name)  # tom

# 查看有几个名引用地址
print(sys.getrefcount(p))

# 想要删除p1对地址的引用
# 只要删除引用就会默认执行del
del p1

# 以下说明只是断掉了p1对地址的引用，而没有回收空间
print('删除p1后打印：', p.name)  # 删除p1后打印： tom

