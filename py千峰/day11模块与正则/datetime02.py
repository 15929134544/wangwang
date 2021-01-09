# datetime:time模块升级
"""
    datetime模块：
        time    时间
        date    日期  （data 数据）
        datetime    日期时间
        timedelta   时间差

"""
import time
import datetime

print(datetime.time.hour)  # 对象

d = datetime.date(2020, 11, 11)
print(datetime.date.day)  # 对象
print(d.day)
print(datetime.date.ctime(d))

# datetime  timedelta
print(datetime.date.today())    # 返回当前的日期

# 时间差值
timedel = datetime.timedelta(hours=2)
timedel = datetime.timedelta(weeks=3)
print(timedel)

now = datetime.datetime.now()   # 得到当前的日期和时间
print(now)
result = now - timedel
print(result)


# 应用
# 缓存：数据库redis   作为缓存    redis.set(key, value, 时间差)
# 会话机制：session

