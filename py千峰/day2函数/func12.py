# 开发：登录验证

import time


islogin = False    # 默认没有登录

# 定于一个装饰器进行付款验证

# 定义一个登录函数


def login():
    username = input("请输入用户名：")
    password = input("请输入用户密码：")
    if username == 'admin' and password == '123456':
        return True
    else:
        return False


def login_required(func):

    def wrapper(*args, **kwargs):
        global islogin
        print("------付款----------")
        # 验证用户是否登录
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print("用户没有登录，不能付款")
            islogin = login()

    return wrapper


@login_required
def pay(money):
    print("正在付款，付款金额是：{}元".format(money))
    print("付款中...")
    time.sleep(2)
    print("付款成功！")


# 调用
pay(10000)

pay(8000)