"""
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

注意：fileter()返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
"""
#例1，在一个list中，删除偶数，只保留奇数
def is_odd(n):
	return n%2 == 1
l = list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15]))
print(l)


#例2，用filter()求素数。
def _odd_iter():
	"""这是一个生成器，并且是一个无限序列"""
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	"""这是一个筛选函数"""
	return lambda x:x%n > 0

def primes():
	"""定义一个生成器，不断返回下一个素数"""
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)

for n in primes():
	if n < 100:
		print(n)
	else:
		break