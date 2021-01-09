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
    global islogin
    if islogin:
        if goodsName:
            # 登录的

            print("成功将{}加入到购物车！".format(goodsName))
        else:
            print("没有选中任何商品")
    else:
        # 没有登录的
        answer = input("是否需要重新登录?：（yes/no）")
        if answer == 'yes':
            # 重新登录
            username = input("请输入用户名：")
            password = input("请输入密码：")

            # 调用login
            islogin = login(username, password)   # 在一个函数里面可以调用另一个函数
        else:
            print("很遗憾，不能添加任何商品")



def login(username, password):
    if username == 'lijiaqi' and password == '123456':
        # 登录成功
        # print("登录成功")
        return True
    else:
        # 登录失败
        # print("登录失败")
        return False


# 调用函数：添加商品到购物车中
islogin = False # 用于判断用户是否登录，默认是没有登录
username = input("请输入用户名：")
password = input("请输入密码：")
islogin = login(username, password)
add_shoppingcart('阿玛尼唇釉')
