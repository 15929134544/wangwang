# """练习"""
# 1.
#
#
# def func(a, *args):
#     print(a, args)
#
#
# # 调用
# func(2, 3, 4, 5)  # 2 (3,4,5)
#
# func(2, [1, 2, 3, 4])  # 2 ([1,2,3,4],)
# # ！！！不管是字符还是数字还是列表，都会被当作一个元素传进元组里面
#
# func(2, 3, [1, 2, 3, 4, 5])  # 2 (3,[1,2,3,4,5])
#
# func(5, 6, (4, 5, 7), 9)  # !!! 5 (6,(4,5,7),9)
# 2.
#
#
# def func(a, b=10, c=3, **kwargs):  # 有关键字的默认值
#     print(a, b, c, kwargs)
#
#
# # 调用
# func(1)  # 1 10 3 {}
#
# func(2, b=10)   # 2 10 3 {}
#
# # func(3, 5, 7, a=1, b=2)     # 变量名不要重名
# # 判断错误：3 5 7 {'a': 1, 'b': 2}
# # 报错：TypeError: func() got multiple values for argument 'a'
# # 这个方法获取了多个a的值
# # multiple意为数量多的
#
# func(3, c=5, b=7)   # 使用默认值关键字时，只要指定对了变量，顺序不重要


3.


def func(a, *args, **kwargs):
    print(a, args, kwargs)


# 调用
t = (1, 2, 3, 4)
func(1, t)  # 1 ((1, 2, 3, 4),) {}

# l = [2, 5, 8]
# func(1, 1, a=9, b=6)    # 报错：获取多个a的值

l = [2, 5, 8]
func(1, 1, c=9, b=6)  # 1 (1,) {'c': 9, 'b': 6}
func(1, *l)  # 1 (2, 5, 8) {}
# 如果想拆列表，在列表前面加个*


"""
总结案例：
courses = ['html', 'mysql', 'python']
"""


def func1(name, *args):  # 装包
    if len(args) > 0:
        for i in args:
            print("{}学过了{}".format(name, i))
    else:
        print("没有学过任何编程知识！")


courses = ['html', 'mysql', 'python']

# 调用函数
func1('困困', *courses)  # 拆包


'''
无参数：
def func():
    pass
    
func()---->调用

有参数：
（1）普通参数：
def func(name, age):
    pass
    
func("aa", 18)---->调用时实参要和形参的个数要一致

（2）可变参数
 A:   def func(*args):
        pass
    
    func()---->调用函数时，参数可以没有，也可以有多个，注意*的不能用关键字参数

B:    def func(**kwargs):
        pass
        
    func(a=1, b=2)---->函数调用时，参数的个数可以没有，也可以多个，注意**的必须
    是关键字参数

C:【扩展情况】：拆包和装包
    def func(*args, **kwargs):
        pass
    
    list = [1,2,3,4]
    dict = {'a': 1, 'b': 2}
    func(*list)
    func(**kwargs)
    
D:混用
    def func(name, *args, **kwargs):
        pass
        
    # 调用
    func('tom')---->name必须赋值

（3）默认值
    def func(name, age=18):
        pass
        
    func('tom')---->tom 18
    func('tom', age = 20)---->关键字赋值
'''
