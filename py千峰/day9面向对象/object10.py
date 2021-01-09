# 多继承的搜索顺序：经典类  新式类

# 经典类：
class P1:
    def foo(self):
        print('p1----foo')

    def bar(self):
        print('p1----bar')


class P2:
    def foo(self):
        print('p2----foo')


class C1(P1, P2):
    pass


class C2(P1, P2):

    def bar(self):
        print('C2-------->bar')


class D(C1, C2):
    pass


d = D()
d.foo()  # p1----foo
d.bar()  # C2-------->bar


# 新式类


class P1(object):
    def foo(self):
        print('p1----foo')

    def bar(self):
        print('p1----bar')


class P2(object):
    def foo(self):
        print('p2----foo')


class C1(P1, P2):
    pass


class C2(P1, P2):

    def bar(self):
        print('C2-------->bar')


class D(C1, C2):
    pass


d = D()
d.foo()
d.bar()

# 在python2时，经典类是从左到右，深度优先，新式类是广度优先
# 在python3中， 两者的搜索顺序没有差别，都是广度优先

