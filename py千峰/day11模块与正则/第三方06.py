# 第三方：pillow
# import pillow     安装第三方：pip install pillow
import requests

# requests拿到的是源代码
response = requests.get('http://www.baidu.com/')

print(response.text)