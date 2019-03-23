import pickle as p

shoplistfile = 'E:\\test\\shoplist.data'

shoplist = ['apple', 'm ango', 'carrot']

f = open(shoplistfile, 'wb')
p.dump(shoplist,f) 
f.close()
del shoplist 

f = open(shoplistfile,"rb")
storedlist = p.load(f)
print(storedlist)
