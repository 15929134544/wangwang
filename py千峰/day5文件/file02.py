# os中的函数
import os

# 获取当前文件所在文件夹的路径
dir = os.getcwd()
print(dir)

# 返回指定目录下所有文件和文件夹的名称
# 保存在列表里
# dirs = os.listdir(r'D:\pythonhello\py千峰\day5文件')
# # ['file01.py', 'file02.py', '__init__.py', '回顾.txt']
# print(dirs)

# 创建文件夹
# # 先判断这个文件是否存在
# if not os.path.exists(r'd:\pythonhello\py千峰\day6文件'):
#     f = os.mkdir(r'd:\pythonhello\py千峰\day6文件')
#     print(f)    # none

# 删除文件夹
# 只能删除空文件夹，否则报错：OSError: [WinError 145]
# 目录不是空的。: 'd:\\pythonhello\\py千峰\\day6文件'
# f = os.rmdir(r'd:\pythonhello\py千峰\day6文件')
# print(f)

# 删除多个目录（在问价夹里面放的是目录）
# # 报错：OSError: [WinError 145] 目录不是空的。: 'd:\\pythonhello\\py千峰\\day6文件'
# f = os.removedirs(r'd:\pythonhello\py千峰\day6文件')
# print(f)

# 还是报错，只能一层一层删除
# 删除文件
# os.remove(r'D:\pythonhello\py千峰\day6文件\aa.py')
#
# 删除day这个文件夹
path = r'D:\pythonhello\py千峰\day6文件\day'

# 得到文件夹里面的所有文件
# filelist = os.listdir(path)
#
# for file in filelist:
#     path1 = os.path.join(path, file)
#     os.remove(path1)
# # for循环遍历完了
# else:
#     # 删除目录
#     os.rmdir(path)
#
# print('删除成功')

# 切换目录
f = os.chdir(r'D:\pythonhello\py千峰\day6文件')
print(f)  # none


# 总结
"""
os模块下的方法：
os.getcwd():获取当前工作文件所在文件夹的路径
os.listdir():浏览当前文件夹
os.mkdir():创建文件夹
os.rmdir():删除一个空文件夹
os.remove():删除一个文件
os.chdir():切换目录


"""
