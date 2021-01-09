'''
    加入购物车
    判断用户是否登录，如果登录则加入购物车成功，否则提示登录再添加

    成功 Ture     失败 False

    def add_shoppingcart(goodsName):
        pass


    def login(username, password):
        pass

'''

# 调用


def add_shoppingcart(goodsName):
    if islogin and goodsName:
        # 登录的
        print("成功将{}加入到购物车！".format(goodsName))
    else:
        # 没有登录的
        print("没有登录，或没有添加任何商品")


def login(username, password):
    if username == 'lijiaqi' and password == '123456':
        # 登录成功
        print("登录成功")
        return True
    else:
        # 登录失败
        print("登录失败")
        return False


# 调用函数：添加商品到购物车中
islogin = False # 用于判断用户是否登录，默认是没有登录
username = input("请输入用户名：")
password = input("请输入密码：")
islogin = login(username, password)
add_shoppingcart('阿玛尼唇釉')

