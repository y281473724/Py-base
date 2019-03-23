#动态语言和静态语言最大的不同，就是函数和类的定义
#不是编译时定义的，而是运行时动态创建的
#type()函数既可以返回一个对象类型，又可以创建出新的类型
#比如我们可通过type()函数创建一个Hello类而无需通过class Hello(object):...的方法

def fn(self,name = 'world'):#先定义函数
	print('Hello,%s.' %name)

#创建一个class对象，type()函数依次传入3个参数：
#1.class的名称；
#2.继承的父类集合，如果只有一个父类，要注意tuple单元素的写法；
#3.class的方法名称与函数绑定，这里把函数fn绑定到方法名hello上。

Hello = type('Hello', (object,), dict(hello = fn))#创建Hello class

h = Hello()
h.hello()