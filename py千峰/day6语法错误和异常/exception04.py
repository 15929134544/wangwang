# 抛出异常 raise

# 注册 用户名必须六位

def register():
    username = input('请输入用户名：')
    if len(username) < 6:
        raise Exception('用户名长度必须是6位以上')
    else:
        print("输入的用户名正确：", username)


# 调用函数
try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')

