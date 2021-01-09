# 函数嵌套
def a():
    print("aaa")


def b():
    # 调用a函数
    a()
    print("bbb")


# 调用函数b
b()