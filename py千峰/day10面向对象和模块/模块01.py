"""
在python中，模块是代码组织的一种方式，把功能相近的函数放到一个文件中，一个文件（.py）就是一个
模块（module），模块名就是文件名去掉后缀.py。这样做的好处是：

（1）提高代码的可复用、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
（2）解决了命名冲突，不同模块中相同的命名不会冲突

常用标准库：

标准库             说明

builtins           内建函数默认加载
math               数学库
random             生成随机数
time               时间
datetime           日期和时间
calendar           日历
hashlib            加密算法
copy               拷贝
functools          常用的工具
os                 操作系统接口
re                 字符串正则匹配
sys                python自身的运行环境
multiprocessing    多进程
threading          多线程
json               编码和解码 Json对象
logging            记录日志、调试


1、自定义模块

2、使用系统的模块


导入模块：
1、import 模块名
    模块名.变量/函数/类

2、from 模块名 import 变量/函数/类
    在代码中可以直接使用变量/函数/类

3、是第二种方式的一种变形
    from 模块名 import *
    *代表该模块所有的内容
    但是如果想限制获取的内容，可以在模块中使用__all__ = [使用*可以访问到的东西]

4、无论是import还是from的形式，都会将模块内容进行加载（如果模块里面涉及函数调用，就会执行）
    如果不希望其进行调用，就会用到__name__
    在自己的模块里面__name__叫__main__
    如果在其他模块中，通过导入的方式调用的话，：__name__:模块名

"""

list1 = [4, 2, 7, 8, 9]
#
# # 导入模块  import 模块名
# import calculate
#
# # 使用模块中的函数  模块名.变量/函数/类
# result = calculate.add(*list1)
# print(result)
#
# # 使用模块的变量
# print(calculate.number)
#
# # 使用模块中的类
# cal = calculate.Calculate(88)
# cal.test()
#
# calculate.Calculate.test1()

# 导入模块中的一部分
# from calculate import add, number, Calculate
# from calculate import number
from calculate import *


result = add(*list1)
print(result)

sum = result + number
print(sum)

cal = Calculate(80)
cal.test()

