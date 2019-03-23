#如果要获得一个对象的所有属性和方法，可以使用dir()函数，
#它返回一个包含字符串的list
l = dir('abc')
#print(l)

#类似__xxx__的属性和方法在Python中有特殊用途，如__len__方法
#返回长度，当调用len()函数获取对象长度时，在len()函数内部，
#它自动调用该对象的__len__()方法
a = len('ABC')
print(a)
b = 'ABC'.__len__()
print(b)

#利用getattr()、setattr()、以及hasattr()，可以直接操作一个对象的状态
class Myobject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
obj = Myobject()

print('有属性x吗？',hasattr(obj,'x'))
print(obj.x)
print('有属性y吗？',hasattr(obj,'y'))
setattr(obj,'y',19)#设置一个属性'y'
print('有属性y吗？',hasattr(obj,'y'))
y = getattr(obj,'y')#获取属性y
print(obj.y)

#可以传入一个default参数，如果属性不存在，则返回默认值
z = getattr(obj,'z',404)
print(z)

#也可以获得对象的方法
print('获取power方法：',getattr(obj,'power'))