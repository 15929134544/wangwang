# 匿名函数:简化函数定义(将原来按照套路要写的代码缩减)
# 格式：lambda(关键字)    参数1，参数2....：运算


# def func():
#     print("aaa")
#
#
# def add(a, b):
#     s = a + b
#     return s


s = lambda a, b: a + b  # s是<function <lambda> at 0x015BBC90>

print(s)  # s就是函数function,就是那个匿名函数

result = s(1, 2)
print(result)

s1 = lambda a, b: a * b
result1 = s1(1, 2)
print(result1)


# 匿名函数可以作为参数出现
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)


# 调用
func(1, 2, lambda a, b: a + b)

# 匿名函数与内置函数的结合使用
# max   sorted  zip...

list1 = [3, 5, 8, 9, 0]
m = max(list1)

print("列表的最大值为:", m)

list2 = [{'a': 1, 'b': 20}, {'a': 13, 'b': 20}, {'a': 9, 'b': 20}, {'a': 29, 'b': 20}]

m = max(list2, key = lambda x: x['a'])
print("最大值为：", m)