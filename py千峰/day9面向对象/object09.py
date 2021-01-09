# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('----------eat1')
#
#     def eat(self, food):
#         print('----------eat', food)
#
# python中有重名的两个方法，类加载时后一个就会将前一个重写（覆盖）
# p = Person('jack')
# p.eat('狮子头')


class Base:
    def test(self):
        print('-----Base----------')


class A(Base):
    def test(self):
        print('AAAAAAAAAAAAA')


class B(Base):
    def test(self):
        print('BBBBBBBBBBBB')


class C(Base):
    def test(self):
        print('CCCCCCCCCCCCCC')


class D(A, B, C):
    pass


d = D()
d.test()  # AAAAAAAAAAAAA

import inspect

# 搜索顺序
print(inspect.getmro(D))

print(D.__mro__)
# c.test1()
# c.test2()

"""
 python允许多继承，
    def 子类（父类1， 父类2...）：
        pass
    
    如果父类中，有相同名称的方法，
         
"""