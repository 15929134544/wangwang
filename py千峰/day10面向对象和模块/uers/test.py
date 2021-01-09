"""
    article包：
        |——models.py
        |——__init__.py
        |——...

    user包：
        |——models.py
            |——User
        |——__init__.py
        |——test.py

    package.py(同级)
"""
# 外用里
# 用户发表文章
# 创建用户对象
# 即使两个模块在同一个包里，导入时也应该通过包.模块导入
from uers.models import User
# from .models import User  # 当前目录下的models里面的User类
# ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package
from article.models import Article

user = User('admin', '123456')  # ----->user就是通过导入User类创建的

# 发表文章，文章对象
article = Article('个人总结', '家伟')

user.publish_article(article)

# 里用外
list1 = [1, 3, 5, 6, 7]

from calculate import add

result = add(*list1)
print(result)