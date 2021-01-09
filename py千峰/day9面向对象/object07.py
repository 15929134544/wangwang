# is a
# base class    父类/基类
"""
继承：
    Student Employee Doctor------>都属于Person类
    相同的代码------>代码冗余，可读性不高

    将相同的代码进行提取---------->Person类

    Student Employee Doctor------>继承Person

    class Student(Person):
        pass


搜索原则：先搜索本类，再搜索父类

特点：
    1、__init__:如果类中不定义init方法，默认调用父类super().__init__()
    2、如果类继承了父类，也需要去定义自己的__init__，
    就需要在子类的__init__中调用父类的__init__
    3、如何去调用父类的__init__:
        super().__init__(参数...)
        super(类名， 对象（self）).__init__(参数...)
    4、如果父类有eat（），子类也定义了一个eat方法，默认搜索的原则：先找当前类，再去找父类
    s.eat()
    override:重写（覆盖）
    父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写

    5、子类的方法中也可以调用父类方法：
        super().方法名(参数)
        
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):

    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print('{}正在学习{}课程'.format(self.name, course))

    def eat(self, food):
        super().eat()
        print(self.name + '正在吃饭...喜欢吃:' + food)


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('jack', 18, 'python1905')
s.run()
s.study('python基础')
s.eat('狮子头盖饭')

e = Employee('tom', 23, 10000, 'king')
e.run()

list1 = ['zhangsan', 'lisi', 'wangwu']
d = Doctor('lucy', 30, list1)
d.run()
