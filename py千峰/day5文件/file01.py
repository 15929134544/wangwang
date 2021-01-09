# os.path

import os

# 判断是否是一个绝对路径
r = os.path.isabs(r'D:\pythonhello\py千峰\day4文件操作\aa.txt')
print(r)

# 获取路径

# dirname = directory 目录/文件夹 name
path = os.path.dirname(__file__)  # 获取当前文件所在文件夹的路径
print(path)

# 通过相对路径得到绝对路径
# D:\pythonhello\py千峰\day5文件\回顾.txt
path = os.path.abspath('回顾.txt')
print(path)

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)

# 当前工作文件所在文件夹的路径
path = os.getcwd()  # 类似于os.path.dirname(__file__)
print(path)

# 判断是否是文件
r = os.path.isfile(os.getcwd())
print(r)

# 判断是否是文件夹
r = os.path.isdir(os.getcwd())
print(r)

# os.path

path = r'D:\pythonhello\py千峰\day5文件\file01.py'

result = os.path.split(path)

print(result[1])  # 文件名
# ('D:\\pythonhello\\py千峰\\day5文件', 'file01.py')
# filename = path[path.rfind('\\')+1:]

# 文件的扩展名（文件类型）
# 分割文件与扩展名
result = os.path.splitext(path)
print(result)  # ('D:\\pythonhello\\py千峰\\day5文件\\file01', '.py')

# 获取文件大小，单位是字节
size = os.path.getsize(path)
print(size)  # 1246

"""
os.path：常用函数

dirname()获取当前文件所在文件夹的路径 = os.getcwd()

join()
result = os.path.join(os.getcwd(), 'file', 'aa.py')
后面允许跟多个，多一个就代表在路径上多一层

split():
（1）获取文件名
os.path.split(path)
（2）获取文件的扩展名
os.path.splitext(path)

os.path.getsize():获取文件大小

os.path.isabs()：判断是否是绝对路径

os.path.file():判断是否是一个文件

os.path.isdir():判断是否是一个文件夹

"""