import json

#把一个python对象变成一个JSON
d = dict(name = 'Muskyo', age = 30, score = 78)
s = json.dumps(d)#dumps()方法返回一个str，内容就是标准的JSON
print('json.dumps():',s)

#同pickle一样，dump()方法可以直接把JSON写入一个file-like Object
#与pickle不同的是，这里不是bytes，不用'wb'
with open('E:\\test\\JSON.txt','w') as f:
	json.dump(d,f)

#把JSON对象反序列化为python对象，用loads()方法或load()方法
ls = json.loads(s)
print('json.loads():',ls)

with  open('E:\\test\\JSON.txt','r') as f:
	ld = json.load(f)
print('json.load():',ld)