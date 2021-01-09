# 地址引用
a = 10  # a叫声明整型变量
b = a


def test():  # 声明函数
    print("--------test---------")


# t = test


# test()
# t()


def func(f):  # f = test
    print(f)  # <function test at 0x00D407C8>
    f()  # --------test---------
    print("-----func")


# 调用
# func(test)

"""
装饰器特点：
1、函数A是作为参数出现的，函数B就接受函数A作为参数
2、要有闭包的特点出现在里面

"""


# 定义一个装饰器
def decorate(func):
    a = 100
    print("wrapper外层测试")

    def wrapper():
        print("---------》111111")
        # func()
        print("---------->222222")
        print(a)

    print("wrapper加载完成")
    return wrapper


# 使用装饰器
@decorate
def house():

    print("我是毛坯房")


"""
1、house是被装饰函数
2、将被装饰函数作为参数传给装饰器
3、执行装饰器函数
4、将返回值赋值给house 
"""

# 调用house函数
house()
print(house)
