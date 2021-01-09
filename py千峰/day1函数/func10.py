# global 变量的范围
# 全局变量  局部变量

# 声明在函数外部的是全局变量，所有函数都可以访问
name = '月月'


def func():
    # 函数内部声明的变量，局部变量，仅限于在函数内部使用

    s = 'abcd'
    s += 'X'
    print(s, name)


def func1():
    global name  # 不修改全局变量，只是获取或者打印。但是如果要修改全局变量。则需要
    # 在函数内部声明：global 变量名
    # 修改后，全局变量的值发生改变
    # print(s, name)
    name += '弹吉他的小美女'
    print(name)
    # 报错：函数内部的变量可以随意修改赋值
    # 但是全局变量不能随便在函数体中修改


def func2():
    name = '小月月'  # 全局变量与局部变量同名了
    name += '弹吉他的小美女'
    print(name)


# print(s)  报错
func1()
func2()
