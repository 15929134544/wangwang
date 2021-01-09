# 模块：os.py
import random

import os
"""
os.path：
os.path.dirname(__file__)获取当前文件所在的文件夹目录
os.path.join(path, '')  返回的是一个拼接后的新路径


"""

# print(os.path)  # 寻找路径
#
# print(os.path.dirname(__file__))  # 获取当前所在文件所在的文件目录（绝对路径）
#
# path = os.path.dirname(__file__)
# print(type(path))  # <class 'str'>

# day3函数/test.py---------->保存在当前文件所在的目录

# with as可以在操作完成后自动关闭文件
with open(r'D:\pythonhello\py千峰\day4文件操作\aa.txt', 'rt') as stream:
    container = stream.read()   # 读取文件内容
    print(stream.name)
    file = stream.name

    # rfind返回要查找的内容最后一次出现的位置
    filename = file[file.rfind('\\')+1:]

    path = os.path.dirname(__file__)

    result = os.path.join(path, filename)   # join用来拼接

    with open(result, 'w') as wstream:
        wstream.write(container)

print('文件复制完成')
