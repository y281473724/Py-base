#__iter__方法返回一个迭代对象，
#然后for循环不断调用该迭代对象的__next__方法拿到循环的下一个值，
#直到遇到StopIteration错误时退出循环

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1#初始化两个计数器a和b

	def __iter__(self):
		return self #实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b#计算下一个值
		if self.a > 10000:#退出循环条件
			raise StopIteration()
		return self.a#返回下一个值

#现在把Fib实例作用于for循环：
for n in Fib():
	print(n)