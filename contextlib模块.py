"""
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()
"""

#编写__enter__和__exit__很繁琐，
# python的标准库contextlib提供了更简单的写法 
#上面的代码可以改写如下：

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query info about %s" %self.name)

@contextmanager
def creat_query(name):
    print("Begin")
    q = Query(name)
    yield q
    print("End")
#@contextmanager这个decorator接受一个generator
#用yield语句把with...as var把变量输出出去，
# 然后with语句就可以正常工作了
with creat_query("Ken") as q:
    q.query()

#如果我们希望在某段代码执行前后自动执行特定代码，
#也可以用@contextmanager实现

@contextmanager
def tag(name):
    print("<%s>" %name)
    yield
    print("<%s>" %name)
with tag("h1"):
    print("hello")
    print("world")

#如果一个对象没有实现上下文，我们就不能把它用于with语句。
#这个时候，可以用close()来把该对象变成上下文对象。
#例如，用with语句使用urlopen():
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("https://www.yalayi.com/gallery/76.html?fr=mtr76")) as page:
    for line in page:
        print(line)