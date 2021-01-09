class Person:
    def __init__(self):
        self.__money = 200
        self.name = '匿名'

    def show1(self):
        print(self.name, self.__money)


class Student(Person):
    def __init__(self):
        # super().__init__()
        # super(Student, self).__init__()
        Person.__init__(self)
        self.__money = 500

    def show(self):
        print('money:', self.__money)


s = Student()
s.show()    # AttributeError: 'Student' object has no attribute '_Student__money'
s.show1()
"""
父类中私有的属性和方法，是不能继承给子类的
"""