# 登录校验

import time


def decorate(func):
    def wrapper(*args, **kwargs):  # 参数不确定怎么办，想把装饰器变成万能的
        print("-------正在校验中-----------")
        time.sleep(2)  # 停顿两秒
        print("校验完毕")
        # 调用原函数
        func(*args, **kwargs)  # 要带*，把元组拆开才能分别给每个参数赋值

    return wrapper


@decorate
def f1(n):
    print("-------f1--------", n)


f1(5)  # TypeError: wrapper() takes 0 positional arguments but 1 was given


# 此时的f1是wrapper


@decorate
def f2(name, age):
    print("------f2----------", (name, age))


f2("lili", 20)


@decorate
def f3(students, cla='1905'):
    for stu in students:
        print(stu)


students = ['lili', 'tom', 'lucy']
f3(students, cla='1904')


@decorate
def f4():
    print("-----------f4")


f4()
