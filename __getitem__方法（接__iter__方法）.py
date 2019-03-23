#使用__iter__方法后，虽然能作用于for循环，
#但是不能当做list来用，比如按下标取出元素，
#此时就要用到__getitem__方法：

class Fib(object):
	def __getitem__(self,n):
		if isinstance(n, int):#n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a

		if isinstance(n, slice):#n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L



#这样就可以按下标访问数列的任意项了
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])
print(f[0:5])
print(f[:10])