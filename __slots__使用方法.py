#Python允许在定义class时，定义一个特殊的__slots__变量，来限制calss能添加的属性。
class Student(object):
	__slots__ = ('name','age')

s = Student()
s.name = 'Muskyo'
s.age = 25
print('name:',s.name,'age:',s.age)
"""
s.score = 99#由于score没有放入到__slots__中，所以不能绑定
"""

#__slots__定义的属性仅对当前类起作用，对继承的子类不起作用
class GraduateStudent(Student):
	pass
g = GraduateStudent()
g.score = 99
print('score:',g.score)