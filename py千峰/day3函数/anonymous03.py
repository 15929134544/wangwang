# 递归函数：在函数里面自己调用自己
"""
总结：
普通函数：def func():
匿名函数：lambda 参数：返回结果
递归函数：普通函数的一种表现形式

特点：
1、递归函数必须要设定一个终点，否则就会无限循环
2、通常都会有一个入口（参数）

"""


def sum(n):  # 1~n
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


# 调用
result = sum(10)
print(result)


s = 0
for i in range(11):
    s += i
print(s)