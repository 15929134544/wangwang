"""
通过列表生成式（列表推导式），我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面的几个元素，那后面绝大多数元素占用的空间都白白浪费了
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出
后续的元素呢？
占用就不必创建完整的list，从而节省大量的空间，
在python中，这种一边循环一边计算的机制，称为生成器：generate


得到生成器的方式：
1、通过列表推导式得到一个生成器


"""

# 得到生成器对象（将[]换成（））
g = (x*3 for x in range(10))
print(type(g))  # <class 'generator'>

# 如何取到生成器里面的值

# 方式一：通过调用__next__()得到一个元素
print(g.__next__())
print(g.__next__())
print(g.__next__())

# 方式二：next(生成器对象)   使用builtins 系统内置函数
# 注意：每调用一次next，则会产生一个元素
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# StopIteration生成器本来就可以产生10个，得到了10个，
# 再调用就会抛出异常