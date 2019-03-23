#计算pi的值
import itertools

def pi(N):
    '计算pi的值'
    sum = 0
    jishu_list = itertools.count(1, 2)
    div_4 = itertools.cycle([4,-4])

    for i in range(N):
        sum += next(div_4)/next(jishu_list)

    return sum

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')