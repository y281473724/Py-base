#python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
import itertools

#count()会创建一个无限的迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 10:
        break

#cycle()会把传入的一个序列无限重复下去
import itertools
cs = itertools.cycle('ABC')
a = 0
for c in cs:
    print(c)
    a += 1
    if a >= 10:
        break

#repeat()负责把一个元素无限重复下去，
# 如果提供第二个参数就可以限定重复次数
import itertools
ns = itertools.repeat('A',5)
for n in ns:
    print(n)

#无限序列虽然可以无限迭代下去，但是可以通过takewhile()等函数
#根据条件判断来截取出一个有限的序列
import itertools
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<10,natuals)
list(ns)

#itertools提供的几个迭代器操作函数更加有用：
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
import itertools
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#grouopby()把迭代器中相邻的重复元素挑出来放在一起
import itertools
for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
#挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
#这两个元素就被认为是在一组的，而函数的返回值作为组的key
#如果忽略大小写分组，可以让元素'A'和'a'返回相同的key：
for key, group in itertools.groupby('AaaBBbcCaAaC', lambda c:c.upper()):
    print(key, list(group))