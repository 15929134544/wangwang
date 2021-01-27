# python的一些内置函数

# l = [1,2,3,4,5,6]
# res = '|'.join(l)
# print(res)

# map 映射
# l = [1,2,3,4,5]
# res = map(lambda x: x**2, l)
# print(list(res))

# zip 拉链
# l1 = [111, 222, 333, 444]
# l2 = ['嫌弃', '刘洋', '小航']
# res = zip(l1, l2)
# print(list(res))  # 以短的为主

# filter 过滤
l = [1, 2, 3, 4, 5, 6, 7, 8]
res = filter(lambda x: x > 3, l)
print(list(res))  # [4, 5, 6, 7, 8]


# reduce不是内置函数  多个进一个出
from functools import reduce

l = [1,2,3,4,5,6]
# res = reduce(lambda x, y: x*y, l)
res = reduce(lambda x,y: x+y,l,100)
print(res)
