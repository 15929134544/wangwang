# random模块

import random

ran = random.random()  # 0-1之间的随机小数
print(ran)

ran = random.randrange(1, 20, 2)  # 不包括20    # randrange(start, end, step)
print(ran)

ran = random.randint(1, 10)  # [1, 10]
print(ran)

list1 = ['feifei', 'xueqiang', 'jiawei', 'apeng', 'awen']
ran = random.choice(list1)  # 随机选择列表内容
print(ran)

pai = ['红桃A', '方片K', '梅花']
random.shuffle(pai) # 打乱顺序
print(pai)

# 验证码   大小写字母与数字的组合


def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])

        code += r
    return code


code = func()
print(code)