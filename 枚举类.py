#为枚举类型定义一个class类型，然后每个常量都是class的唯一实例。

from enum import Enum, unique

Moth = Enum('Moth', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', \
		'Aug', 'Sep','Oct', 'Nov', 'Dec'))
#此时，我们获得了Moth类型的枚举类，可以直接使用Moth.Jan来引用一个常量
#或者枚举他的所有成员

for name, member in Moth.__members__.items():
	print(name,'=>',member,',',member.value)
#value属性是自动赋值给成员的int常量，默认从1开始

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类

@unique#@unique装饰器帮助检查保证没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

#访问方法有很多种

day1 = Weekday.Mon
print('day1:',day1)
print('day1.value:',day1.value)
print('day1 == Weekday.Wed：',day1 == Weekday.Wed)
print('Weekday(3):',Weekday(3))

for name, member in Weekday.__members__.items():
	print(name,'=>',member,'--',member.value)