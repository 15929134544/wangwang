# 持久化保存：文件
# 列表、元组、字典------->都不叫持久化，因为他们都是从内存里面来的

# 用户注册
def register():
    username = input('输入用户名：')
    password = input('输入密码：')
    repassword = input('输入确认密码：')

    if password == repassword:
        # 保存信息
        with open(r'D:\pythonhello\py千峰\day6\book\user.txt', 'a') as wstream:
            wstream.write('{} {}\n'.format(username, password))
        print("用户注册成功")
    else:
        print('密码不一致')


# 用户登录
def login():
    username = input('输入用户名：')
    password = input('输入密码：')

    if username and password:
        with open(r'D:\pythonhello\py千峰\day6\book\user.txt') as rsteam:
            while True:
                user = rsteam.readline()

                if not user:
                    print('用户名或密码输入有误')
                    break

                input_usrname = '{} {}\n'.format(username, password)

                if user == input_usrname:
                    print('用户登录成功')
                    break


def show_books():
    print("---------------图书馆里面的图书有----------------")
    # encoding='utf-8'
    with open(r'D:\pythonhello\py千峰\day6\book\books.txt', 'r', encoding='utf-8') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')


# 调用函数
# register()
# login()
show_books()
