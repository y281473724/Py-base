#去除文件中的空格
class clearspe:
    """去除文档中的空格"""
    def __init__(self,fname):
        self.fname = fname
    def do(self):
        f = open(self.fname,"r")
        ls = f.read()
        f.close()
        lt = ls.replace(' ','')
        f = open(self.fname,"w")
        f.write(lt)
        f.close()

