# 类中方法：动作
# 种类：普通方法   类方法     静态方法    魔术方法
"""
self 表示自己
普通方法格式：
def 方法名（self,[参数， 参数...]）：
    pass
"""


class Phone:
    brand = 'xiaomi'
    price = 4999
    type = 'mate 80'

    # Phone类里面的方法：call
    def call(self):
        print('self------->', self) # <__main__.Phone object at 0x02F09950>
        print('正在打电话...')


phone1 = Phone()
print(phone1, '------1--------')
print(phone1.brand)
phone1.call()


print('***************************')
phone2 = Phone()
print(phone2, '------2--------')
print(phone2.brand)
phone2.call()
