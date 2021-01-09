# 语法错误和异常
# 语法错误：

# 异常：程序运行的时候报出来的错误，xxxError

# 异常处理
"""
格式：
    try:
        可能出现异常的代码

    except：
        如果有异常执行的代码

    finally（可以有，可以没有）:
        无论有没有异常，都会执行的代码

情况1：
    try:
        有可能会产生多种异常
    except 异常类型1：
        pass
    except 异常类型2：
        pass
    except: Exception:
        pass

    如果是多个except，异常的类型需要注意，最大的Exception要放到最后

情况2：获取Exception的错误原因
    try:
        有可能会产生多种异常
    except 异常类型1：
        pass
    except 异常类型2：
        pass
    except: Exception as err:
        print('错误的原因是', err)------>err的内容就是错误原因

    pop from empty list------>从空列表中删除信息

情况3：
    try:
        有可能会产生多种异常
    except 异常类型1：
        pass
    except 异常类型2：
        pass
    else:
        如果try中没有异常才会执行的代码

注意：如果使用else，则在try中使用的代码就不能使用return




"""


def func():
    try:
        n1 = int(input('请输入第一个数字：'))
        n2 = int(input('请输入第二个数字：'))

    except:
        print("必须输入数字！！！")


func()
print('------------->')