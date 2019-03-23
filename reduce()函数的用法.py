"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这
个函数必须接收两个参数，reduce把结果继续和序列的
下一个元素做累积计算。在 Python3 中，reduce() 函数
已经被从全局名字空间里移除了，它现在被放置在
functools 模块里，如果想要使用它，则需要通过引入
functools 模块来调用 reduce() 函数：
"""
from functools import reduce
#方法一
def add(x,y):
    return x+y
s = reduce(add,[1, 3, 5, 7, 9])
print(s)

#方法二
def fn(x,y):
    return x*10 + y
l = reduce(fn,[1, 3, 5, 7, 9])
print(l)

#方法三：reduce()配合map()，把str转换为int
def  char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, \
              '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
m = reduce(fn,map(char2num,'13579'))
print(m)
