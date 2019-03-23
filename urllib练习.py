from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
    return json.loads(data.decode('utf-8'))


URL = 'http://news-at.zhihu.com/api/4/news/latest'
data = fetch_data(URL)
print(data)
