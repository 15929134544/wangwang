# 局部和全局变量
# 如果全局变量如果是不可变的，在函数中进行修改需要加global关键字
# 如果全局变量是可变的，在函数中修改的时候就不需要添加global
name = '月月'

list1 = [1, 2, 4, 6]


def func():
    name = '蕊蕊'
    print(name)
    print(list1)


def func1():
    global name
    print(name)
    name += '真漂亮'

    # 修改列表
    list1.append(8)
    print(list1)


def func2():
    name = 'lucy'
    name += 'xjioe'
    print(name) # 自己的

    global name
    print(name)
    # 报错
    # SyntaxError: name 'name' is used prior to global declaration
    # 解决：如果想要在函数体内使用全局变量，尽量避开让局部变量和全局变量重名


# 调用
func1()
#
func()

func2()
