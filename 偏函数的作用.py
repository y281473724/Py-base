"""
functools.partial的作用就是，把一个函数的某些参数
给固定住（也就是设置默认值），返回一个新的函数，调
用这个新函数会更简单。
"""
import functools
int2 = functools.partial(int,base=2)
print(int2('10000'))
"""
注意到上面的int2函数仅仅是把base的默认值设置为2，
但也可以在函数调动时设置其他值
"""
print(int2('101010101010',base = 10))
"""
最后,创建偏函数时,可以接收函数对象  *args和**kw这三个参数
"""
max2 = functools.partial(max,10)
print(max2(5,6,7))
"""
总结:当函数的参数个数太多时,可以使用functools.partial创建
一个新函数,这个函数可以固定住原函数的部分参数从而在调用时更
简单
""""