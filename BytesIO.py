#StringIO操作的只能是str，如果要操作二进制数据，需要BytesIO
#BytesIO实现了在内存中读写bytes

from io import BytesIO
f = BytesIO()
f1 = f.write('中文'.encode('utf-8'))
#写入的不是str，而是经过utf-8编码的bytes
print(f1)
print(f.getvalue())

fr = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f2 = fr.read()
print(f2)