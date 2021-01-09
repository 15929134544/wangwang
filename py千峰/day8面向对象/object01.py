"""
面向对象：

程序          现实中
对象----->   具体的事物


现实中的事物---->转成电脑程序
世间万物皆对象

好处：代码更灵活，复用性更高

    面向对象：
    类：
    对象：
    属性：
    方法：

对象：xx的手机、xx的手机...

对象的集合--->共同的特征： 品牌、 颜色、大小、价格     动作：打电话、发短信、上网、打游戏

作为一个类别出现：手机类
                学生类

    特征：姓名、年龄、性别、身高、血型、婚否...---->属性
    动作：刷抖音、敲代码、打电话、看书...---->方法

    多个对象--->提取对象共同的特征和动作----->封装到一个类中





"""
# 所有的类名要求首字母大写，多个单词使用驼峰式命名法
"""
格式：
class 类名[(父类)]：
    属性：特征
    
    方法：动作

"""


class Phone:

    # 属性
    brand = 'huawei'
    # 方法


# 使用类对象
yp = Phone()
print(yp.brand)
# 改变属性的值
yp.brand = 'iphone'
print(yp.brand)

feifei = Phone()
print(feifei.brand)
feifei.brand = 'iphone xxs'
print(feifei.brand)


xiaowei = Phone()
print(xiaowei.brand)