# 补充类方法
"""
静态方法：很类似于类方法
1、需要装饰器@staticmethod
2、类中的静态方法是无需传递参数（cls,self都不需要）
3、也只能访问类的属性和方法，而无法访问对象的
4、加载时机同类方法

总结：
静态方法和类方法的区别是什么？
不同：
1、静态方法的装饰器@staticmethod ，类方法的装饰器是@classmethod
2、类方法的参数是cls(所在的类)，静态方法没有参数
相同：
1、类方法和静态方法都可以通过类名访问类属性和类方法，但是对象的是无法访问的
2、都可以通过类名去调用访问
3、都可以在创建对象之前使用，因为是不依赖于对象的


普通方法与两者的区别：
不同之处：
1、没有装饰器
2、普通方法永远都依赖于对象，因为每一个普通方法都有一个self
3、只有创建了对象，才可以调用普通方法，否则无法调用

"""


class Person:
    __age = 18  # 变成私有属性（外界不能访问，只能在类里面访问）

    def __init__(self, name):
        self.name = name

    def show(self):
        Person.__age = 15
        print('-------->', Person.__age)

    @classmethod
    def update_age(cls):
        cls.__age = 20  # 对类的私有属性进行修改
        print('-------->类方法', Person.__age)

    @staticmethod
    def test():
        print('---------->静态方法')
        # print(self.name)    # 语法错误
        print(Person.__age, p.__age)


p = Person('jack')
p.show()


Person.test()
