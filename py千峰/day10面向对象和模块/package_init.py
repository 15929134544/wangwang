"""
__init__.py文件

当导入包的时候，默认调用__init__.py文件
作用：
1、当导入包的时候，把一些初始化的函数/变量/类定义在__init__.py文件里面
2、此文件中的函数/变量等的访问，只需要通过包名.函数...
3、结合__all__ = [通过*可以访问的模块]
"""

# import uers  # --------->user的__init
#
# # from uers.models import User
#
# uers.creat_app()
# uers.printA()

# from 模块 import * 表示可以使用模块里面的所有内容，如果没有定义__all__的话，
#                      但是如果添加__all__，只有__all__里面的东西可以访问

# from 包 import *   表示该包中的内容（模块）是不能访问的，就需要在__init__.py文件中定义
#                    __all__ = ['可以通过*访问的模块']
from uers import *  # 说明包里面的所有东西都导入过来了，但是不能使用包里面的模块
# 此时需要结合__all__和__init__.py文件

user = models.User('admin', '123456')
user.show()
