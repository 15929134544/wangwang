# 私有化
"""
封装：将属性私有化，并定义公有化的方法去访问
1、私有化属性
2、定义共有的set和get方法


__属性：就是将属性私有化，访问范围只限于类中

私有化的好处：
1、隐藏属性不被外界随意的修改
2、也可以修改:通过一个函数完成
   def setXXX(self, xxx):
        3、进行筛选赋值的内容
        if xxx是否符合条件：
            赋值
        else：
            不赋值
3、如果想获取具体的某一个属性
    使用get函数
    def getXXX(self):
        return self.__xx

"""


class Student:

    # __age = 18  # 类属性

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 59

    # 定义共有的set和get方法
    # set是为了赋值
    def setAge(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            print('年龄不在规定范围内')

    # get是为了取值

    def getAge(self):
        return self.__age

    # 修改名字的时候长度必须是6位
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字不是6位')

    def getName(self):
        return self.__name

    def __str__(self):
        return '姓名:{}, 年龄：{}, 考试分数：{}'.format(self.__name, self.__age, self.__score)


yupeng = Student('yupeng', 18)

# 只能看到，不能修改，也不能单独访问
print(yupeng)  # 姓名:yupeng, 年龄：18, 考试分数：59
yupeng.setAge(20)
print(yupeng)  # 姓名:yupeng, 年龄：20, 考试分数：59
yupeng.setName('xiaopeng')

# 就想拿到yupeng的年龄
print(yupeng.getAge())

