class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 59

    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字不是6位')

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{}, 年龄：{}, 考试分数：{}'.format(self.__name, self.__age, self.__score)

    # attribute:__init__ __str__ setName  getName


s = Student('yupeng', 18)

print(s)

print(dir(Student))

print(__name__)

print(s._Student__age)  # 其实它就是__age，只不过系统自动改名字了
# 不建议以此种方式访问，真正的访问要通过set和get两种方法

# 都可以用来查看对象里的方法和属性
print(s.__dir__())
print(dir(s))
