# 返回值：将函数中运送的系欸过return（扔）出来
def add(a, b):
    result = a + b
    # print(result) # 仅仅限于打印在终端上，辅助程序员开发时查看，但是外部是无法使用的
    return result  # 返出结果的关键字return


# 调用函数
x = add(6, 10)
print(x)


'''
:return 返回值 
1.return后面可以是一个参数， 接收的时候x = add(6, 2)
2.return后面也可以是多个参数，如果是多个参数，底层会将多个参数放进一个元组，
将元组作为一个整体返回
3.接收的时候也可以是多个：return 'hello', 'world'
x, y = ('hello', 'world')
x = 'hello'  y = 'world'
'''