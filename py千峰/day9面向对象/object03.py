# 在开发中看到一些私有化处理：装饰器
class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__score = 59

    # 先有getxxx
    @property
    def age(self):
        return self.__age

    # 再有set，因为set依赖于get，所以必须先有get再有set
    @age.setter
    def age(self, age):
        if 0 < age < 100:

            self.__age = age
        else:
            print('不在规定的范围内')

    # def setAge(self, age):
    #     if 0 < age < 100:
    #         self.__age = age
    #     else:
    #         print('不在规定的范围内')
    #
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名:{}, 年龄：{}, 考试分数：{}'.format(self.name, self.__age, self.__score)


s = Student('peng', 20)
# 没有私有化
s.name = 'xiaopeng'
print(s.name)

# 利用@property装饰器，可以将私有的像非私有的一样调用和赋值
s.age = 30
print(s.age)
print(s.__dir__())
# 私有化赋值
# s.setAge(30)
# print(s.getAge())
