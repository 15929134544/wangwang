# 装饰器带有参数,就是三层
"""
带参数的装饰器是三层的
最外层的函数负责接受装饰器的参数
里面的内容还是原装饰器的内容

"""
# 不带参数，就是两层


def outer(a):  # 第一层 负责接受装饰器的参数
    def decorate(func):  # 第二层 负责接受函数

        def wrapper(*args, **kwargs):  # 第三层 负责接受函数的参数
            func()
            print("--------铺砖{}块".format(a))

        return wrapper  # 返出第三层

    return decorate  # 返出第二层


@outer(10)  # 也可a = 10
def house():
    print("我是毛坯房...")


@outer(100)
def street():
    print("黑泉路")


# 调用函数
house()
street()
