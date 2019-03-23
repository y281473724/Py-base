#任何类，只要定义一个__call__()方法，就可以直接对实例进行调用

class Student(object):
	def __init__(self,name):
		self.name = name

	def __call__(self):
		print("My name is: %s" %self.name)

#调用方法如下：
s = Student('Muskyo')
print(s())#self参数不要传入

#对实例进行调用就好比对一个函数进行调用一样
#判断一个对象是否能被调用，可以用callable()函数
#能被调用的就是callable（可调用）对象

a = callable(s)
b = callable(max)
c = callable([1,2,3])
d = callable(None)
e = callable('str')
print(a,b,c,d,e)