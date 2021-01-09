# 列表推导式 字典推导式   集合推导式
# 旧的列表---------> 新的列表

# 1、列表推导式: 格式：[表达式 for 变量 in 旧的列表]
# 或者[表达式 for 变量 in 旧的列表 if 条件]

# 过滤掉长度<=3的人名
names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob', 'ha']
result = [name for name in names if len(name) > 3]
print(result)

# capitalize()将首字母大写
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 将1-100之间能够被3和5整除的，组成一个新的列表
newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)

# 0-5的偶数    0-10的奇数
# [(偶数, 奇数), (), ()...]
newlist = [(x, y) for x in range(5) if x% 2 == 0 for y in range(10) if y% 2 != 0]
print(newlist)


# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]----->[3, 6, 9, 5]
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
# 此时的i是一个数组
newlist = [i[-1] for i in list1]


dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}

list1 = [dict1, dict2, dict3, dict4]

# if薪资>5000加200，低于等于5000加500
newlist = [employee['salary']+200 if employee['salary']>5000 else employee['salary']+500 for employee in list1 ]



"""
def func():
    newlist = []
    for name in names
        if len(name)>3:
            newlist.append(name)
    return newlist
    
    
def func1():
    newlist = [] 
    for i in range(5):  # 偶数
        if i% 2 == 0:
            for j in range(10): # 奇数
                if j% 2 != 0:
                    newlist.append((i, j))
    return newlist   
"""


# 集合推导式 {}类似于列表推导式，在列表推导式的基础上，添加了一个去除重复项的功能

list1 = [1, 2, 1, 3, 5, 2, 1]

set1 = {x for x in list1 if x>=5}
print(set1)


# 字典推导式
"""
注意：返回值的形式（值：值）
"""
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}

# 将key和value进行交换

# !!!items()将key和value一对一对的取出
newdict = {value: key for key, value in dict1.items()}
print(newdict)