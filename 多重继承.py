#在设计类的继承关系时，主线都是单一继承下来的，但是如果要加入额外的功能，
#通过多重继承就可以实现。这种设计通常称为Mixin
class Animal(object):#动物
	pass


class Mammal(Animal):#哺乳动物，继承Animal
	pass


class Bird(Animal):#鸟类，继承Animal
	pass

class Dog(Mammal,Runable):#狗，继承Mammal和Runable
	pass

class Bat(Mammal,Flyable):#蝙蝠，继承Mammal和Flyable
	pass

class Parrot(Bird,Flyable):#鹦鹉，继承Bird和Flyable
	pass

class Ostrich(Bird,Runable):#鸵鸟，继承Bird和和Runable
	pass

class Runable(objec):#能跑的
	def run(self):
		print('Runing...')


class Flyable(object):#能飞的
	def fly(self):
		print('Flying...')

