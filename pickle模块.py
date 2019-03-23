import pickle

#把一个对象序列化并写入文件
d = dict(name='Muskyo', age=30, score=78)
#pickle.dunmps()方法把任意对象序列化成一个bytes
s = pickle.dumps(d)
print('序列化：',s)#输出的是bytes

#或者可以用pickle.dump()直接把对象序列化后写入一个file-like Object
with open('E:\\test\\dump.txt','wb') as f:
	pickle.dump(d,f)


#把对象从磁盘读到内存，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化
#或者直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
with open('E:\\test\\dump.txt','rb') as f:#注意是"rb"
	d = pickle.load(f)
print('反序列化：',d)

#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
#并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，
#不能成功地反序列化也没关系。