from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

L = []

class MyHTMLParser(HTMLParser):
	"""docstring for MyHTMLParser"""

	global L
	def __init__(self):
		super(MyHTMLParser, self).__init__()
		self.__parsedata = '' #设置一个空标签



	def handle_starttag(self, tag, attrs):#处理开始标签
		if tag == 'p':
			self.__parsedata = 'name'



	def handle_endtag(self, tag):
		self.__parsedata = ''

	def handle_data(self, data):
		if self.__parsedata == 'name':
			L.append(data)




parser = MyHTMLParser()
URL1 = 'http://www.sohu.com/a/301221060_100160903?sec=wd&spm=smpc.author.fd-d.1.155255397371617O0Hww'
URL2 = 'https://yuwen.chazidian.com/yuedu89639/'
with request.urlopen(URL2, timeout = 15) as f:
	data = f.read()

parser.feed(data.decode('utf-8'))

print('\n'.join(L))

		