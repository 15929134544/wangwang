# 函数综合应用
'''
    用户登录
    输入用户名
    输入密码
    输入验证码-----》 封装成一个函数

'''

# 定义验证码生成函数

import random


def generate_checkcode(n):
    s = '7894561230qwertyuiopasdfghjklzxcvbnmQWERTYIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        # n代表循环几次
        ran = random.randint(0, len(s)-1)   # 是个闭区间
        code += s[ran]
    return code


# 定义登录函数
def login():
    username = input("输入一个用户名：")
    password = input("输入用户密码：")
    # 得到一个验证码
    code = generate_checkcode(5)    # 函数间的调用
    print("验证码是:", code)
    code1 = input("输入验证码：")
    # 验证
    if code.lower() == code1.lower():
        # 验证码正确
        if username == 'lijiaqi' and password == '123456':
            print("用户登录成功")
        else:
            print("用户名或者密码有误")
    else:
        print("验证码有误")


# 调用
login()