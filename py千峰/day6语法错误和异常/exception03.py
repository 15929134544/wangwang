# 异常情况4
"""
# 文件操作 stream = open(...)   stream.read()   stream.close()
# 数据库操作：close()
try:
    pass
except:
    pass
finally:不管有没有异常都会执行的代码
    pass


"""


def func():
    stream = None
    try:
        stream = open(r'D:\pythonhello\py千峰\day6\book\user.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('---------finally---------')
        if stream:
            stream.close()
        return 3


# 调用函数
x = func()
print(x)