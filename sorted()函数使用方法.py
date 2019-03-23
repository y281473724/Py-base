"""
Python内置的sorted()函数可以对list进行排序(默认从小到大)
此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
"""
#例1：
lt = sorted([36, 5, -12, 9, -21])
print(lt)

#例2：
lt = sorted([36, 5, -12, 9, -21], key=abs)
print(lt)

#例3：
#默认情况下，对字符串排序，是按照ASCII的大小比较的，
#由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
#字符串大小比较方法：从第一个字符开始，位置一一对应比较编码大小，最后比较长度
ls = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(ls)

#例4：忽略大小写，并且从大到小排序
ls = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse = True)
print(ls)