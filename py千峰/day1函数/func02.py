# # 可变参数 + 关键字参数
#
# def add(a, b=10):  # 关键字参数，此时的10是默认值""
#     result = a + b
#     print(result)
#
#
# # 调用
# add(5)
#
# add(4, 7)  # a = 4, b = 7   # 此时7会覆盖b原来的默认值
#
#
# def add1(a, b=10, c=4):
#     result = a + b + c
#     print(a, b, c)
#     print(result)
#
#
# # 调用
# add1(1)
#
# add1(1, 5)  # 是给b赋值5
#
# # 想给c赋值而不是给b赋值
# add1(1, 6)  # 默认6赋给b了
# add1(1, c=6)  # 如果想让6赋给c，可以通过使用关键字指定

# 函数：打印每位同学的姓名和年龄(字典存放)
students = {"001": ("蔡徐坤", 21), "002": ("王源", 19),
            "003": ("王俊凯", 20), "004": ("易烊千玺", 19)}


def print_boys(name, persons):
    print("{}喜欢的小鲜肉有：".format(name))
    if isinstance(persons, dict):
        values = persons.values()
        for name, age in values:
            # format函数用于字符串的格式化
            print("{}的年龄是{}".format(name, age))


# 调用
print_boys("蕊蕊", students)
#
#
# def func(**kwargs):  # key words arguments也叫可变参数
#     print(kwargs)
#
#
# # 调用的时候必须这样赋值
# func(a=1, b=2, c=3)  # 关键字参数
# func()  # {}
#
# func(a=1)  # {'a': 1}
#
# func(a=1, b=2)  # {'a': 1, 'b': 2}

# # 想传进一个字典
# dict1 = {"001": "python", "002": "java", "003": "c语言", "004": "go语言"}
# ！！！字典的键值对的key必须是string
# # func(dict1)   # 报错
# func(**dict1)

