from collections import Counter

f = open("E:\\test\\佳人.txt","r")
ls = f.read()
f.close()

d = Counter(ls)
print(d)
