"""
版本二可以提取出带名字的Email地址：

<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
"""
import re
def name_of_email(addr):
	return re.match(r'^<?(\w+\s?\w+)>?\s*\.*\w*?\@([a-zA-Z]+)(.org)$',addr).group(1)




# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')