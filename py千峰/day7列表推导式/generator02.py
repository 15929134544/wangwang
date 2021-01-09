# g = (x * 3 for x in range(10))
#
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print("没有更多元素啦！")
#         break


# 定义生成器的方式二：借助函数完成
# 只要函数中出现关键字yield，就不是函数，叫生成器
# 斐波那契数列
"""
步骤：
1、定义一个函数，函数中要使用yield关键字
2、调用函数，接收调用的结果
3、得到的结果就是生成器
4、借助于next()或者__next__()得到元素
"""


# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  # return n + yield 暂停
#
#
# g = func()
# print(g)    # <generator object func at 0x02E36EB0> 说明g是一个生成器对象
# print(next(g))
# print(next(g))


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1

    return '没有更多元素了'    # return就是在得到StopIteration后的提示信息
    # StopIteration: 没有更多元素了


g = fib(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # StopIteration
