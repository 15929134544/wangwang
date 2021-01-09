# 作用域
a = 100


def func(b):
    a = 10

    def inner_func():
        a = 1
        print(max, a, b)

    # inner_func()
    return inner_func


# 调用外部函数
f = func(7)
f()
