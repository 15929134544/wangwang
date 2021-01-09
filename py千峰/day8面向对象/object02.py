# 定义类和属性

# 定义类
class Student:
    # 类属性（在模型里面）
    name = 'xiaowei'
    age = 2


# 使用类创建对象
xiaowei = Student()

# 动态创建对象属性，通过赋值操作，赋值操作只会作用在对象空间里面
# 调用的时候，先找自己空间的，然后再去模型空间去找
# 如果自己的空间有，则不会去模型空间去找
xiaowei.age = 18
print(xiaowei.age)


ypeng = Student()

ypeng.name = 'xiaopengpeng'
print(ypeng.name)
print(ypeng.age)

ypeng.age = 1
print(ypeng.age)


# 改变类属性的初始值
Student.name = 'feifei'

ruirui = Student()
print(ruirui.name)  # feifei

