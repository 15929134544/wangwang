# 类方法
"""
普通方法：也是属于类，但是依赖于self，通过对象调用
类方法：也属于类，不依赖于self，参数是cls
对于类方法，不需要对象也可以调用

类方法特点：
1、定义需要依赖装饰器@classmethod
2、类方法中的参数不是一个对象，而是一个类
3、类方法中只可以使用类属性(不能访问对象属性)
4、类方法中可否使用普通方法？不能


类方法的作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要去完成一些动作/功能，
就可以放在类方法里面

"""


class Dog:
    aa = 'aaa'

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print('{}在院子里跑来跑去'.format(self.nickname))

    def eat(self):
        print("吃饭")
        self.run()  # 类中，方法的调用通过self.方法名（）

    @classmethod
    def test(cls):  # cls  class
        print(cls)  # <class '__main__.Dog'>
        print('--------->')
        # self.run()

        # print(cls.nickname)
        # AttributeError: type object 'Dog' has no attribute 'nickname'


# d = Dog('大黄')
# d.run()
#
# d.test()

# 类属性通过类名调用
Dog.aa = ''
# 也可以用类名调用类方法
Dog.test()
