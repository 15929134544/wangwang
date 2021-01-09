# 写操作
"""
stream = open(r'D:\pythonhello\py千峰\day4文件操作\aa.txt', 'w')
mode是w模式，表示的就是写操作

方法：
write（内容）：每次都会将原来的内容清空，再将当前内容写入

writelines（Iterable(可迭代的)）：没有换行的效果，只能自己加换行符


如果mode = 'a'

表示追加（不会清空之前的内容）

"""

stream = open(r'D:\pythonhello\py千峰\day4文件操作\aa.txt', 'w')

# 三个引号的就是保留格式
s = '''
你好！
    欢迎来到澳门博彩赌场，赠送给你一个金币
        赌王：高进
        
'''
result = stream.write(s)
print(result)

stream.write('龙五')

stream.writelines(['赌神高进\n', '赌侠小刀\n', '赌圣周星星\n'])

stream.close()  # 释放管道资源    释放之后不能进行任何文件操作
