a = 100  # 全局变量
print(globals())


def func():
    b = 99

    def inner_func():
        global a
        nonlocal b
        c = 88
        # 尝试修改
        c += 12
        b += 1
        a += 1

        # 尝试去打印
        print(a, b, c)

    inner_func()

    # 使用locals（）内置函数进行查看，可以看到在当前函数声明的内容有哪些
    # locals是一个字典。key:value
    print(locals())  # {'inner_func': <function func.<locals>.
    # inner_func at 0x02F6BC90>, 'b': 100}


# 调用函数
func()
