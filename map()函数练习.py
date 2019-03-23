#练习1
"""
利用map()函数，把用户输入的不规范的英文
名字，变为首字母大写，其他小写的规范名字。
"""
def normalize(name):
    return name[:1].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#练习2
"""编写一个prod()函数，可以接受一个list并利用
reduce()求积"""
from functools import reduce
def prod(L):
    def pro(x,y):
        return x*y
    return reduce(pro,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#练习3
"""利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456"""
def str2float(s):
    def fn(x,y):
        return x*10 + y
    s1 = map(int,s.split('.')[0])
    s2 = map(int,s.split('.')[1])
    return reduce(fn,s1) + reduce (fn,s2)/1000

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
