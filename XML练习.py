
#链接失效,作业没法做啊  - - !!!!!!

from xml.parsers.expat import ParserCreate
from urllib import request

def parseXml(xml_str):
	print(xml_str)
	return{
	'city': '?',
	'forecast': [
		{
			'date': '2017-11-17',
			'high': 43,
			'low': 26
		},
		{
			'date': '2017-11-18',
			'high': 41,
			'low': 20
		},
		{
			'date': '2017-11-19',
			'high': 43,
			'low': 19
		}
	]
	}

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout = 4) as f:
	data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'