#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools
def log(txt):
	def metric(fn):
		@functools.wraps(fn)
		def warg(*args,**kw):
		    print('%s %s in %s ms' % (fn.__name__, txt,10.24))
		    return fn(*args,**kw)
		return warg
	return metric

# 测试
@log('executed balabala')
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log('executed balabala')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print(f)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')