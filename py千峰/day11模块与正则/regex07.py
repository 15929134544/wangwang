# qq = input('输入你的qq号码：')
#
# # 验证号码长度
# if len(qq) >= 5 and qq[0] != '0':
#     print('合法的')
# else:
#     print('不合法的')

import re

msg = '娜扎热巴戴斯佟丽娅'

pattern = re.compile('佟丽娅')

pattern.match(msg)

# 使用正则re模块方法：match

s = '娜扎热巴戴斯佟丽娅'

result = re.match('佟丽娅', s)
print(result)  # None
# match是从头开始匹配的，只要开头不匹配，就返回none

result = re.search('佟丽娅', s)  # search进行正则字符串匹配的方法，匹配的是整个字符串
print(result)

print(result.span())  # span是匹配的位置

print(result.group())  # 使用group方法来提取匹配的数据
print(result.groups())

# 提取符合a2b结构的部分

msg = 'ad484da5dsa87dsa4das78'

result = re.findall('[a-z][0-9]+[a-z]', msg)
print(result)

# qq号验证5-11 开头不能是0
qq = '14944689962'
result = re.match('^[1-9][0-9]{4, 10}$', qq)
print(result)

# 用户名可以是字母或者数字，不能是数字开头，用户名长度必须6位以上[0-9a-zA-Z]

username = '#$admin001#$'
# result = re.match('[a-zA-Z][0-9a-zA-Z]{5,}$', username)  # 带上$就会匹配到结尾
result1 = re.search('^[a-zA-Z]\\w{5,}$', username)  # 带上^和$就会匹配从头到尾
print(result1)

msg = 'aa.py ab.txt bb.py kk.png uu.py'
result = re.findall(r'\w*\.py\b', msg)
print(result)

"""
总结：
    .表示任意字符除换行符之外
    ^表示开头
    $表示结尾
    []表示范围  [abc]表示a/b/c    [a-z]   [a-z#$]
    
    正则预定义：
    \s:  空白字符(空格)
    \b: 表示边界
    \d: 数字
    \w: word 表示[0-9a-zA-Z]
    
    
    大写反面：\S 非空格     \D:非数字
    
    '\w[0-9]'------->\w和[0-9]各自只能匹配一个字母
    
    量词：
    *：>=0
    +:>=1
    ？:0,1次
    
    手机号码正则：
    re.match('1[35789]\d{9}$', phone)
    
    {m}:固定的m位
    {m，}：>=m位
    {m， n}：m <= phone <= n
    
    
"""
