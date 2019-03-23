import base64

def safe_base64_decode(s):
    n = len(s)%4
    if n != 0:
        for i in range(4-n):
            s += b'='#bytes类型直接加在后面就行了
    return base64.b64decode(s)



# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')