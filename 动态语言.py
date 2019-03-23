#正常情况下，当我们定义了一个class，创建了一个class实例后，
#我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student(object):
	pass

s = Student()

#尝试给实例绑定一个属性
s.name = 'Muskyo'
print('s的名字是：',s.name)

#还可以绑定方法
def set_age(self,age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)#调用实例方法
print('s的年龄是：',s.age)

