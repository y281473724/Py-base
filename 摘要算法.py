"""
摘要算法又称哈希算法、散列算法。它通过一个函数，
把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

摘要算法是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，
目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，
计算f(data)很容易，但通过digest反推data却非常困难。而且，
对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
"""

#以常见的摘要算法MD5为例，计算出一个字符串的MD5值
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的

#MD5是最常见的摘要算法，速度很快，生成的结果是固定的128bit字节，
#通常用一个32位的16进制字符串表示
#另一种常见的摘要算法是SHA1。调用SHA1和调用MD5完全类似：
import hashlib

sha1 = hashlib.sha1()
sha1.update("how to use sha1 in ".encode('utf-8'))
sha1.update("python hashlib? ".encode('utf-8'))
print(sha1.hexdigest())
#SHA1的结果是160bit字节，通常用一个40位的16进制字符串表示。