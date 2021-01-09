# map函数

list1 = [1, 2, 5, 8, 9, 4, 0]
result = map(lambda x: x + 2, list1)
print(list(result))  # [3, 4, 7, 10, 11, 6, 2]

# for i, index in enumerate(list1):
#     list1[index] += 2


func = lambda x: x if x % 2 == 0 else x + 1
result1 = func(5)
print(result1)

# 对列表中的奇数进行+1操作
result2 = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result2))

# for index, i in enumerate(list1):
#     if i % 2 != 0:
#         list1[index] += 1
#
# print(list1)


# reduce（）函数：对列表（不仅仅是列表，是对可迭代的元素）中的元素进行加减乘除运算的函数

from functools import reduce

tuple1 = (3, 5, 7, 8, 9)

result2 = reduce(lambda x, y: x + y, tuple1)

print(result2)  # 32

tuple2 = (1,)

result3 = reduce(lambda x, y: x + y, tuple2, 10)  # 11

print(result3)

# 动手测试减法

tuple1 = (3, 5, 7, 8, 9)

result4 = reduce(lambda x, y: x - y, tuple1)

print(result4)  # 32

tuple2 = (1,)

result5 = reduce(lambda x, y: x - y, tuple2, 10)  # 11

print(result5)

# 过滤器
# filter()函数
list1 = [12, 5, 89, 15, 56]

result = filter(lambda x: x > 10, list1)
print(list(result))  # [12, 89, 15, 56]

list3 = [12, 5, 89, 15, 56]

# def func(list3):
#     list2 = []
#     for i in list3:
#         if i > 10:
#             list2.append(i)
#
#     return list2
#
#
# result = func(list3)
# print(result)


students = [
            {'name': 'tom', 'age': 20},
            {'name': 'lucy', 'age': 19},
            {'name': 'lily', 'age': 13},
            {'name': 'mark', 'age': 21},
            {'name': 'jack', 'age': 23},
            {'name': 'steven', 'age': 18}
]


# 找出所有年龄大于二十岁的学生

# 用过滤器

result = filter(lambda x: x['age'] > 20, students)
print(list(result))
# 返回的是一个对象，所以必须转成列表


# 按照年龄从小到大排序

students = sorted(students, key=lambda x: x['age'])

print(students)

# 倒序    students = sorted(students, key=lambda x: x['age']， reverse = True)


"""
总结：都会使用到lambda
前三个用到key
max():
min()
sorted()：排序

map()：同意对列表里面的每一个元素进行一些操作
reduce()：对列表元素进行累加/减
filter()：过滤
"""



