import json, logging

class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Muskyo',30, 78)
try:
	print(json.dumps(s))
except TypeError as t:
	logging.exception(t)
#此时s是类的实例化对象，
#默认情况下，json的dumps方法不知道如何将类的实例变为一个JSON的{}对象

#因此，需要为Student专门写一个转换函数，再把函数传进去
def studict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

#这样将Student的实例先通过studict()函数转换成dict，然后就可以序列化为JSON
print(json.dumps(s,default=studict))#注意该语句的写法！

#另外，class的实例一般都有一个__dict__属性，它就是一个dict
#用来存储实例变量，除非定义了__slots__的class
print(json.dumps(s,default = lambda obj:obj.__dict__))

#------------------------------------------
#如果要把JSON反序列化为一个Student对象实例，load()方法首次转换出一个dict对象
#然后传入的object_hook函数把dict转换成Student实例
def dictstu(d):
	return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook = dictstu))

#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
obj = dict(name='小小',属性='力量',职业='法师')
s = json.dumps(obj,ensure_ascii=True)
print(s)