import urllib.request
 
url = "http://www.baidu.com/s?ie=utf-8&wd=python"
page = urllib.request.urlopen(url)
mybytes = page.read()
encoding = "utf-8"
print(mybytes.decode(encoding))
page.close()