from wsgiref.simple_server import make_server


def index():
    return 'index'


def login():
    return 'login'


def error():
    return '404 error'


# url与函数的对应关系


urls = [
    ('/index', index),
    ('/login', login),
]


def run(env, response):
    """
    :param env: 请求相关的所有数据
    :param response:响应相关的所有数据
    :return:返回给浏览器的数据
    """
    # print(env)  # env是一个大字典 wsgiref模块帮你处理好http格式的数据，封装成了字典让你更加方便的操作
    # 从env中取
    response('200 OK', [])  # 响应首行+响应头
    current_path = env.get('PATH_INFO')
    # if current_path == '/index':
    #     return [b'index']
    # elif current_path == '/login':
    #     return [b'login']
    # return [b'404 error']
    # 定义一个变量 存储匹配到的函数名
    func = None
    for url in urls:  # url (),()
        if current_path == url[0]:
            # 将url对应的函数名赋值给func
            func = url[1]
            break  # 结束当前循环(匹配到一个之后应该立刻结束for循环)
    # 判断一下func是否有值
    if func:
        res = func()
    else:
        res = error()
    return [res.encode('utf-8')]


if __name__ == '__main__':
    server = make_server('127.0.0.1', 8080, run)
    """
    会实时监听127.0.0.1：8080地址 只要有客户端来了
    都会交给run函数处理(加括号触发run函数的运行)
    
    flask启动源码
            make_server('127.0.0.1', 8080, obj)
            __call__ 
    """
    server.serve_forever()  # 启动服务端
