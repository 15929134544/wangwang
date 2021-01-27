import socket


server = socket.socket()  # TCP 三次握手四次挥手
server.bind(('127.0.0.1',8080)) # IP协议 以太网协议 端口协议
server.listen(5)    # 池的概念 进程池  线程池


while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    # print(data) # 是二进制数据
    data = data.decode('utf-8') # 变成字符串
    # 获取字符串中特定的内容   正则  如果字符串有规律也可以考虑用切割
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    current_path = data.split(' ')[1]    # 拿到了一个数组，第二个就是用户输入的后缀
    # print(current_path)
    if current_path == '/index':
        # conn.send(b'index heiheihei')
        with open(r'01 myhtml.html') as f:
            conn.send(f.read())
    elif current_path == '/login':
        conn.send(b'login')
    else:
        # 你直接忽略favicon.ico
        conn.send(b'hello web')
    conn.close()
