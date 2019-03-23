import base64, struct
bmp_data = base64.b64decode("""
Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAA
SCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9
//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwA
fAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8A
Hz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB
8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//
f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//
3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/
9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//
f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/
AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwA
fP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/
AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwA
fAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AH
z/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9
//3//f/9//3//f/9//3//f/9//38AAA==
""")
def bmp_info(data):
    
    d = struct.unpack_from('<ccIIIIIIHH', data)
    print(d)
    return {
        'width': d[6],
        'height': d[7],
        'color': d[9]
    }
# 测试
bi = bmp_info(bmp_data)

assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
