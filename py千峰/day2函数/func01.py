# 内部函数
"""
特点:(1):可以访问外部函数的变量
（2）：内部函数可以修改外部函数可变类型的变量
（3）：内部函数修改全局不可变变量时，需要在内部函数声明一个global
        内部函数修改外部函数的不可变的变量时，需要在内部函数中声明一个nonlocal
（4）：locals()就是来查看本地变量有哪些，以字典的形式输出打印
globals()查看全局变量有哪些，以字典的我形式输出，（注意里面会有一些系统的键值对）
"""


def func():
    # 声明变量
    n = 100  # 局部变量

    list1 = [1, 2, 3, 4]    # 局部变量

    # 声明内部函数
    def inner_func():
        nonlocal n
        # 枚举函数enumerate，可以同时遍历下标和值
        for index, i in enumerate(list1):
            # 对list1里面的每个元素加5
            list1[index] = i + n
        # 对列表里面的元素进行排序
        list1.sort()

        # 修改n的变量
        n += 1

    # 调用一下内部的函数
    inner_func()

    print("打印老大的值：", n)
    print("打印老二的值：", list1)


# 调用
func()