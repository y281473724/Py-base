#多进程和多线程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在每个进程中，互不影响
#而多线程中，所有变量都有线程共享，所以，任何一个变量都可以被任何一个线程修改
#因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，把内容改乱了

import time, threading

#假定这是银行存款
balance = 0
def change_it(n):
	#先存后取，结果应该为0
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		change_it(n)

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
"""
初始值 balance = 0

t1: x1 = balance + 5 # x1 = 0 + 5 = 5
t1: balance = x1     # balance = 5
t1: x1 = balance - 5 # x1 = 5 - 5 = 0
t1: balance = x1     # balance = 0

t2: x2 = balance + 8 # x2 = 0 + 8 = 8
t2: balance = x2     # balance = 8
t2: x2 = balance - 8 # x2 = 8 - 8 = 0
t2: balance = x2     # balance = 0

结果 balance = 0

但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，
线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
"""