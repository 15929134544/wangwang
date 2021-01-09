# 装饰器
"""
    加入购物车、付款、修改收货地址...
    判断用户登录状态，

"""


def func(num):
    a = 100

    def inner_func():
        nonlocal a
        nonlocal num

        num += 1
        for i in range(num):
            a += 1

        print("修改后的a的值为：", a)

    return inner_func


# 调用函数
x = func(5)

x()

# 定义：
# 函数作为参数
a = 50

f1 = func(50)   # a是一个实参
print(f1)

# 地址引用
a = 10  # a叫声明整型变量
b = a


def test(): # 声明函数
    print("--------test---------")


t = test
# test()
# t()


def func(f):
    print(f)
    f()
    print("-----func")
    



t = test()