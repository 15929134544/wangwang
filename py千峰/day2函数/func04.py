# 闭包

"""
条件：
1、外部函数中定义了内部函数
2、外部函数是有返回值的
3、返回的值是内部函数名
4、内部函数还引用了外部函数的变量
"""


def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print("相加之后的结果是：", s)

    return inner_func


# 调用
x = func(6, 9)  # x此时就是inner_func函数
# 调用返出来的内部函数
x()
