#在定义数据库字段类的时候，往往需要对其中的类属性进行限制，
#一般用get和set方法来写。

"""
class Student(object):

	def get_score(self):
		return self.__score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self.__score = value

#调用方法：
s = Student()
s.set_score(60)#OK!
print('score is :',s.get_score())


s.set_score(999)
print('score is :',s.get_score())

"""

#但是这样写太麻烦了，还要set然后get....为了方便，使用@propert来帮忙！
class  Student1(object):

	@property
	def score(self):
		return self.__score
#这样一来，get方法经过@property的装饰后变成了属性
#而property本身又创建了另一个装饰器@score.setter，
#负责把set方法变成给属性赋值，如下：

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self.__score = value
		
#调用时就不用再set然后get了。。
s1 = Student1()
s1.score = 60#实际上转化为s1.set_score(60)
print("s1 score :",s1.score)#实际上转化为s1.get_score()