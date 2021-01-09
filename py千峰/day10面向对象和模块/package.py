# 文件夹   包
# 文件夹：非py文件     包：py文件
# 一个包中可以存放多个模块，而一个模块里面可以放多个类/函数
# 包含关系：项目> 包> 模块>类/函数/变量

# 使用包中模块中的User类
# 两种使用方式：
# (1)
# from uers import models
#
# u = models.User('admin', '123456')
# u.show()

# (2)
from uers.models import User

u = User('admin', '123456')
u.show()


# 使用Article类
from article.models import Article

a = Article('西游记', '吴承恩')
a.show()

"""
    article包：
        |——models.py
        |——__init__.py
        |——...
        
    user包：
        |——models.py
        |——__init__.py
        |——...
        
    package.py(同级)
    
    导入的方式：
        1、from 包 import 模块
        2、from 包.模块 import 类|函数|变量
        3、from 包.模块 import *
        
    
    __all__ = []是结合import*来使用的，也只针对它起作用
"""