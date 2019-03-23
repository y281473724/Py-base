#__enter和__exit__可以实现上下文管理，例如下面的class实现了这两个方法
class Query(object):

    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print("Begin")
        return self

    def __exit__(self, exc_typ, exc_value, traceback):
        if exc_typ:
            print("Error")
        else:
            print("End")
    
    def query(self):
        print("Query info about $s..."%self.name)

#定义了方法后，就可以把自己写的资源对象用于with语句
with Query("Ken") as q:
    q.query()