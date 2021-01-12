"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

join函数：
1.join()函数
    对字符串、列表、元组、字典进行替换
2.os.path.join()
    对文件路径进行拼接

split函数：切割
split('', num)
第一个参数是以什么切割
第二个参数是切割几次
"""


def replaceSpace(s):
    return '%20'.join(s.split(' '))


s = 'We Are Happy'
res = replaceSpace(s)
print(res)