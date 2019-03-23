""" 
Scoket是网络编程的一个抽象概念.通常我们用一个Scoket表示'打开了一个网络链接',
而打开一个Socket需要知道目标计算机的IP地址和端口号,再指定协议类型即可.
大多数连接都是可靠的TCP连接.创建TCP连接时,主要发起连接的叫客户端,
被动响应连接的叫服务器.
"""

# 创建一个基于TCP连接的Scoket:
#导入socket库:
import socket

#创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接:
s.connect(('www.sina.com.cn', 80))#参数是一个tuple,包含地址和端口

#AF_INET指定使用IPv4协议,如果要用IPv6,就指定为AF_INET6.
#SOCK_STRAM指定使用面向流的TCP协议.

#客户端要发起TCP连接,必须知道服务器的IP地址和端口号.
#新浪网站的IP地址可以用域名自动转换到IP地址,
#而作为服务器,提供什么样的服务,端口号就必须固定下来.
#80端口是Web服务的标准端口,其他的例如:SMTP是25,FTP是21
#端口号小于1024的是Internet标准服务的端口,端口号大于1024的,可以任意使用

#建立TCP连接后,我们就可以向新浪服务器发送请求,要求返回首页内容
s.send(b'GET / http/1.1\r\nHost:www.sina.com.cn\r\nConnection: close\r\n\r\n')

#TCP连接创建的是双向通道，双方都可同时给对方发送数据.
# 但是谁先发谁后发,怎么协调,要根据具体的协议来决定.
# 例如,HTTP协议规定客户端必须先发请求给服务器,服务器接到后才发数据给客户端
# 发送的文本格式必须符合HTTP标准.如果格式没有问题,就可以接收服务器返回的数据了
buffer = []
while True:
    #每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#接收数据时,调用recv(max)方法,一次最多接收指定的字节数.
#因此,在一个while循环中反复接收,知道recv()返回空数据
#当数据接收完后,调用close()方法关闭Socket.
s.close()
#接收到的数据包括HTTP头和网页本身，
# 我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open("E:\\test\\sina.html", 'wb') as f:
    f.write(html)