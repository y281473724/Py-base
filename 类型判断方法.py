#方法1：
print(type(123))
print(type('abc'))
print(type([1,2,3]))
print(type(None))
print(type(abs))

#方法2：
import types
def fn():
	pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

#方法3
print(isinstance(1,int))
print(isinstance((1,2,3),(list,tuple)))
