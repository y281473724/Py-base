from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re



class MyHTMLParser(HTMLParser):
	"""docstring for MyHTMLParser"""
	def __init__(self):
		super(MyHTMLParser,self).__init__()
		self.__parsedata = '' #设置一个空的标志位

	def handle_starttag(self,tag,attrs):
		if ('class', 'even-title') in attrs:
			self.__parsedata = 'name' #通过属性判断如果标签是我们要找的标签,设置标志

		if tag == 'time':
			self.__parsedata = 'time'

		if ('class', 'say-no-more') in attrs:
			self.__parsedata = 'year'

		if ('class', 'event-location') in attrs:
			self.__parsedata = 'locations'

	def handle_endtag(self,tag):
		self.__parsedata = '' #在标签结束时,把标志位清空

	def handle_data(self,data):
		if self.__parsedata == 'name':
			print('会议名称:%s' %data) #通过标志位判断,打印输出内容

		if self.__parsedata == 'time':
			print('会议时间:%s' %data) 

		if self.__parsedata == 'year':
			if re.match(r'\s\d{4}', data):
				print('会议年份:%s' %data.strip())#因为后面还有两组say-na-more,后面data却不是年份信息,所以用正则测试一下 

		if self.__parsedata == 'locations':
			print('会议地点:%s' %data) 
			print('----------------------------------------')

parser = MyHTMLParser()



with request.urlopen('https://www.python.org/events/python-events/', timeout = 15) as f:
	data = f.read()

parser.feed(data.decode('utf-8'))
