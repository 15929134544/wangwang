# 文件复制
"""
源文件：D:\pythonhello\py千峰\day4文件操作\aa.txt'
目标文件：D:\pythonhello\py千峰\day4文件操作\bb.txt'

with的好处：
with结合open使用，可以帮助我们自动释放资源

注意：
open只能复制一个文件，不能批量复制，比如复制一个文件夹
"""

# with as可以在操作完成后自动关闭文件
with open(r'D:\pythonhello\py千峰\day4文件操作\aa.txt', 'rt') as stream:
    container = stream.read()   # 读取文件内容

    with open(r'D:\pythonhello\py千峰\day4文件操作\bb.txt', 'w') as wstream:
        wstream.write(container)

print('文件复制完成')


