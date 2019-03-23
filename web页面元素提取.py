#导入模块
import urllib.request
from contextlib import closing
import re

#导入网址
url = "https://www.yalayi.com/gallery/76.html?fr=mtr76https://www.yalayi.com/gallery/76.html?fr=mtr76"

#新建文本储存网页
f = open("E:\\url.txt", "wb")

#通过链接获取整个网页
with closing(urllib.request.urlopen(url)) as page:
    for line in page:
        f.write(line)
f.close()

#读取文件内容，并将结果转化为一个分行列表
def getLines(inPath):
    with open(inPath, "r" , encoding = 'utf-8') as f:
        ls = f.readlines()
    return ls

def extractImage(htmllist):
    urls = []
    for i in htmllist:
        mre = re.match(r'^[<img class=](.*)[alt="作品结束图" >]$',i)
        if mre != None:
            m = mre.group(1)
            url = m.split("'")
            for line in url:
                if 'jpg' in line:
                    urls.append(line)
    
    return urls

def showResults(urls):
    count = 0
    for url in urls:
        print("第{:2}个url：{}".format(count, url))
        count += 1

def saveResults(filepath, urls):
    with open(filepath, "w") as f:
        for url in urls:
            f.write(url+'\n')   

def main():
    htmlpath = "E:\\url.txt"
    filepath = "E:\\result.txt"
    htmlList = getLines(htmlpath)
    imageUrls = extractImage(htmlList)
    showResults(imageUrls)
    saveResults(filepath,imageUrls)

main()

