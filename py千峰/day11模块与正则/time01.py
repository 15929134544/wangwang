# time模块
# 1、时间戳
import time

t = time.time()
print(t)
# time.sleep(3)  # 延迟执行
t1 = time.time()
print(t1)

# 将时间戳转成字符串的形式
s = time.ctime(t)
print(s)  # Wed Nov 11 17:10:54 2020

# 将时间戳转成元组方式
t2 = time.localtime(t)
print(t2)
print(t2.tm_yday)   # 可以取元组里面的值
# (tm_year=2020,tm_mon=11, tm_mday=11, tm_hour=17, tm_min=12, tm_sec=33,
# tm_wday=2, tm_yday=316, tm_isdst=0)

# 将元组转成时间戳
tt = time.mktime(t2)
print(tt)

# 将元组转成字符串
s = time.strftime('%Y-%m-%d %H-%M-%S')   # 年月日格式
print(s)

# 将字符串转成元组的方式
r = time.strptime('2020/11/11', '%Y/%m/%d')
print(r)

"""
总结：
time模块：
    重点：
    time()
    sleep()
    strftime()# 将元组转成字符串
    s = time.strftime('%Y-%m-%d %H-%M-%S')   # 年月日格式
    
    了解：
    元组：t = time.localtime(t)
    t.tm_year    t.tm_mon
    
    
"""