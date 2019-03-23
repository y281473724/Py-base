#这是一个模块文件
#可以把它用在其他程序中
#这个模块的作用是把温度转为华氏温度
def ctof(celsius):
	"""把温度转为华氏温度"""
    fahrenheit=celsius*9.0/5+32
    return fahrenheit
