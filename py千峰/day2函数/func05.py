# 闭包的应用
# 闭包：
"""
作用：
1、保存返回返回闭包时的状态（外层函数变量）

"""


def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print("相加之后的结果是：", s)

    return inner_func


# 调用
x = func(6, 9)  # x此时就是inner_func函数
x1 = func(2, 8)
# 调用返出来的内部函数
x()  # 相加之后的结果是： 25
x1()  # 相加之后的结果是： 20


# 闭包的例子
# 计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] += 1
        print("当前是第{}次访问".format(container[0]))

    return add_one


# 内部函数就是一个计数器
count = generate_count()
count()  # 第一次访问
count()  # 第二次访问
