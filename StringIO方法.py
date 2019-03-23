#把str写入StringIO，需要先创建一个StringIO
from io import StringIO

f = StringIO()
s1 = f.write("hello")
s2 = f.write(" ")
s3 = f.write("world!")
print(s1)
print(s2)
print(s3)
print(f.getvalue())#getvalue()方法用于获得写入后的str



#要读取StringIO，可以用一个str初始化StringIO，然后读取
fr = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = fr.readline()
	if s == '':
		break
	print(s.strip())