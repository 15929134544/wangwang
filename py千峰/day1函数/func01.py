# 可变参数（里面的参数内容是不确定的，个数也是不确定的）

# def add(a, b):
#     pass


# add(1)
# 报错： add丢失了一个b
# 函数调用后面有小块阴影，说明这块有问题
# add(1, 2, 3)  报错
# 所以这个函数只能传两个参数


# 定义方式：
def add(name, *args):
    print(args)
    # （）空元组
    # sum = 0
    # if len(args) > 0:
    #     for i in args:
    #         sum += i
    #     print("累加和是:sum:%d" % sum)
    # else:
    #     print("没有元素可计算", sum)


# add()  # ()
add(1)  # (1,)
add(1, 2, 3)  # (1, 2, 3 )
add(1, 2, 3, 4)  # (1, 2, 3, 4)

# 调用
add("菲菲", 1, 2, 3)
# a, *b = 1, 2, 3, 4
# 注意：可变参数必须放在前面:  name, *args
