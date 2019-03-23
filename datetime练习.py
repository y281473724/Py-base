"""
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
以及一个时区信息如UTC+5:00，均是str，
请编写一个函数将其转换为timestamp：
"""
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    UTC = re.match(r'^(UTC)(.\d+):(0*)$',tz_str).group(2)
    iutc = int(UTC)
    dt_iutc = timezone(timedelta(hours = iutc))
    dt_utc = dt.replace(tzinfo = dt_iutc)
    print(dt_utc)
    dt_stamp = dt_utc.timestamp()
    return dt_stamp

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
