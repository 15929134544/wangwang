# 加密算法:md5  sha1    sha256(都是单向的)
# base64
import hashlib

msg = 'yupeng中午一起吃饭去！'
md5 = hashlib.md5(msg.encode('utf-8'))  # md5不支持中文，将其转换为utf-8格式

# 取出十六进制的表示方式
print(md5.hexdigest())  # ae1c387be826c6ce165d994b8c304e47

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())

password = '123456'

list1 = []

sha256 = hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())

pwd = input('请输入密码：')
sha256 = hashlib.sha256(pwd.encode('utf-8'))
pwd = sha256.hexdigest()

for i in list1:
    if pwd == i:
        print('登录成功')