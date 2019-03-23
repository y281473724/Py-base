#虽然Python提供了Unicode表示的str和bytes两种数据类型
#并且可以通过encode()和decode()方法转换,但是在不知道编码的情况下,
#对bytes做decode()不好做
#对于未知编码的bytes,要把它换成str,需要先'猜测'编码,
#chardet这个第三方库就是用来检测编码的,简单易用

#当我们拿到一个bytes时,就可以对其检测编码,用chardet检测编码,只需要一行代码
import chardet

c = chardet.detect(b'Hello,world!')
#print(c)
#输出结果:{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
#结果显示检测出的编码是acsii,confidence字段表示检测的概率,1.0是100%

#试试检测GBK编码的中文:
data = '锄禾日当午,汗滴禾下土'.encode('gbk')
c = chardet.detect(data)
#print(c)
#输出结果:{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
#检测编码是GB2312,注意:GBK是GB2312的超集,两者是同一种编码,检测正确的概率是74%

#对UTF-8编码进行检测:
data = '锄禾日当午,汗滴禾下土'.encode('utf-8')
c = chardet.detect(data)
#print(c)

#再试试对日文进行检测:
data = '最新の主要ニュース'.encode('euc-jp')
c = chardet.detect(data)
#print(c)


#课件,用chardet检测编码,简单易用,获取到编码后,再转换为str,就可以方便后续处理.