# 可迭代对象：1、生成器   2、元组、列表、集合、字典、字符串
# 如何判断一个对象是可迭代的？

from collections.abc import Iterable

# from collections import Iterable会警告，加上.abc即可

list1 = [1, 4, 7, 8, 8]

f = isinstance(list1, Iterable)
print(f)

f = isinstance('abc', Iterable)
print(f)

f = isinstance(100, Iterable)
print(f)

# 判断生成器是否可迭代
g = (x + 1 for x in range(10))
f = isinstance(g, Iterable)
print(f)  # True

# 迭代器
"""
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历位置的对象
特点：
迭代器对象从集合的第一个元素开始访问，直到所有元素被访问结束。
迭代器只能往前不能后退。

可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator

可迭代的是不是就是迭代器？

可迭代的分成两类：

生成器：是可迭代的，也是一个迭代器

list是可迭代的，但不是迭代器

list------->iter(list)--------->迭代器
"""

list1 = [1, 2, 3, 4, 5]
# print(next(list1))  # 'list' object is not an iterator

list1 = iter(list1) # 通过iter函数将可迭代的变成了一个迭代器

print(next(list1))

"""
生成器与迭代器之间的关系（图）：
迭代器是一个大的部分，生成器只是它里面的一小部分，
列表、元组、集合、字典等等，是可迭代的，但都不是迭代器
通过iter函数可以将他们变成迭代器
迭代器就是可以被next函数调用，并且不断返回下一个值的对象称为迭代器
生成器就是为了节省内存，一个个的拿到元素
产生生成器的方式有两种：
一、通过列表推导式
二、借助函数
"""