# 文件操作
"""
文件上传
保存log

系统函数
open（file, mode, buffering, encoding）

读操作：
open(path/filename, ‘rt’)------->返回值：stream（流对象）
如果文件和file是同级目录的情况下，用filename，否则用绝对路径
mode默认是rt，就是读文本文件
可以将他理解为一个管道，可以从管道里面调东西

container = stream.read()------->读取管道中的内容部分
print(container)

注意：
如果传递的path/filename有误，则会报错FileNotFoundError
如果是图片，则不能使用默认的读取方式，应该使用mode = 'rb'（二进制的形式）

总结：
read():读取所有内容
readline():每次读取一行内容
readlines():读取所有行，保存到列表中
readable():判断是否可读

"""

# stream = open(r'D:\pythonhello\py千峰\day4文件操作\aa.txt')  # pycharm做读的动作

# container = stream.read()  # 表示的就是读流里面的内容
# print(container)

# result = stream.readable()  # 判断这个文件是不是可读的
# print(result)  # True

# while True:
#     line = stream.readline()
#     print(line)  # hello world
#     if not line:
#         break


# lines = stream.readlines()  # 保存到列表里面
# print(lines)  # ['hello world\n', 'hello kitty\n', 'hello baby\n', 'hello hello']
# # 前面如果使用了readline方法，readlines只会输出一个[]
#
# # 遍历列表
# for i in lines:
#     print(i)

# 可以读取图片吗？
# 读取图片时，不能使用默认的读取方式，应该转成二进制
stream = open(r'C:\Users\25974\Desktop\timg.jpg', 'rb')  # rb表示以二进制读

container = stream.read()
print(container)