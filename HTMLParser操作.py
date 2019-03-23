from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		print('开始标签<%s>,属性:%s' %(tag,attrs))
		return ('开始标签<%s>,属性:%s' %(tag,attrs))

	def handle_endtag(self, tag):
		print('结束标签<%s>' %tag)
		return ('结束标签<%s>' %tag)

	def handle_startendtag(self, tag, attrs):
		print('开始结束标签<%s>' %tag)

	def handle_data(self, data):
		print('数据',data)

	def handle_comment(self, data):
		print('注释<!--',data, '-->')

	def handle_entityref(self, name):
		print('特殊符号&%s:' %name)

urlfile = "E:\\test\\HTMLparser练习网页.txt"
with open(urlfile,'r') as f:
	u = f.read()
"""
urlfile = '''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''
"""
parser = MyHTMLParser()
parser.feed(u)

