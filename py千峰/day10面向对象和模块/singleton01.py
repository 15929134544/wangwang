# 单例（单个对象）模式：在程序开发时，无论创建多少个对象，用的都是同一块内存空间
# 开发模式：单例模式
"""
单例其实是对于内存的一种优化，保证创建的对象都使用同一块地址

"""

# class Student:
#     pass
#
#
# s = Student()
#
# s1 = Student()
#
# print(s)  # <__main__.Student object at 0x01A0B150>
# print(s1)  # <__main__.Student object at 0x01A111D0>
# # 地址不同，说明每创建一个对象，就占用一块新的内存空间

class Singleton:
    # 私有化   单例的地址就存在于__instance中
    __instance = None
    name = 'jack'

    # 重写__new__
    def __new__(cls):
        print('----------__new__')

        # return object.__init__()  组织它产生新的地址即可
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            print('----------------------1')
            print(cls.__instance)
            return cls.__instance

        return cls.__instance

    def show(self, n):
        print('----------show', Singleton.name, n)


s = Singleton()
s1 = Singleton()

print(s)
print(s1)

s.show(5)
s1.show(7)