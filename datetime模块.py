from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
#datetime是模块，在datetime模块中还包含一个datetime类
#datetime.now()返回当前日期和时间，其类型是datetime

dt = datetime(2015, 4, 19, 12, 20)
print(dt)
#指定某个日期和事件，直接用参数构造一个datetime

#datetime转换为timestamp（时间戳）
"""
在计算机中，时间实际上是用数字表示的。
我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
记为0（1970年以前的时间timestamp为负数），
当前时间就是相对于epoch time的秒数，称为timestamp。
"""
#把一个datetime类型转换为timestamp需调用timestamp()方法
st = dt.timestamp()
print(st)
#如果有小数位，小数位表示毫秒数

#把timestamp转换为datetime,使用datetime提供的fromtimestamp()方法
print(datetime.fromtimestamp(st))#本地时间
print(datetime.utcfromtimestamp(st))#UTC时间

#str转换为datetime
"""
很多时候，用户输入的日期和时间是字符串，
要处理日期和时间，首先必须把str转换为datetime。
转换方法是通过datetime.strptime()实现，
需要一个日期和时间的格式化字符串：
"""
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str
"""
如果已经有了datetime对象，要把它格式化为字符串显示给用户，
就需要转换为str，转换方法是通过strftime()实现的，
同样需要一个日期和时间的格式化字符串：
"""
dday = now.strftime("%a, %b %d %H:%M")
print(dday)
#注意区别strptime()和strftime()使用上的不同

#datetime加减
"""
对日期和时间进行加减实际上就是把datetime往后或往前计算，
得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类
"""
from datetime import timedelta
print(now)#now在之前就已经赋值了

now = now + timedelta(hours = 10)
print(now)

now = now - timedelta(days = 1)
print(now)

now = now + timedelta(days = 2, hours = 20)
print(now)

#本地时间转换为UTC时间
"""
一个datetime类型有一个时区属性tzinfo，但是默认为None，
所以无法区分这个datetime到底是哪个时区，
除非强行给datetime设置一个时区：
"""
from datetime import timezone
tz_utf_8 = timezone(timedelta(hours=8))#创建时区UTC+8:00
now = datetime.now()
print(now)
tz_time = now.replace(tzinfo=tz_utf_8)#强制设置为UTC+8:00
print(tz_time)
#如果系统时区恰好是UTC+8:00,那么上述代码就是正确的
#否则不能强制设置为UTC+8:00

#时区转换
"""
可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
"""
#拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)

#astimezone()将时区转为北京时间：
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)

#小结
"""
datetime表示的时间需要时区信息才能确定一个特定的时间，
否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，
因为timestamp的值与时区完全无关。
"""
