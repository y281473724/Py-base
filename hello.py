#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module'

__author__ = 'Muskyo'

#第1-2行是标准注释.第四行是一个字符串,表示模块的文档注释.
#任何模块代码的第一个字符串都被视为模块的文档注释
#第六行使用__author__变量把作者写进去
#下面是真正的代码:
import sys  #使用sys模块的第一步,导入sys模块
def test():
    args = sys.argv
#argv变量用list存储了命令行的所有参数,第一个参数永远是该.py文件的名称
    if len(args) == 1:
        print("Hello world!")
    elif len(args) == 2:
        print("Hello,%s"%args[1])
    else:
        print("Too many arguments")

if __name__ == '__main__':
    test()
