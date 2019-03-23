#动态返回一个属性
class Student(object):

	def __init__(self):
		self.name = 'Muskyo'

	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda:25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
		#如果找不到，__getattr__默认返回的是None，可以给它加一个新的错误返回

#当调用不存在的对象时，python解释器会试图调用__getattr__来获得属性
s = Student()
print(s.name)
print(s.score)#调用不存在的对象
print(s.age())#返回函数时，调用方式变了
print(s.abc)#__getattr__找不到这个属性，返回指定的错误

#注意，只有在没有找到属性的情况下，才调用__getattr__
