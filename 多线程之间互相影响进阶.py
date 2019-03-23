#要确保balance计算正确，就要给change_it上一把锁，当某个线程开始执行change_it时
#该线程因为获得了锁，因此其他线程不能同时执行change_it，只能等待
#直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻
#最多只有一个线程持有该锁，所以不会造成修改的冲突。
#创建一个锁通过threading.Lock()来实现。

import time, threading

balance = 0
lock = threading.Lock()


def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		#先要获得锁：
		lock.acquire()
		try:
			change_it(n)
		finally:
			#改完之后释放锁：
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5,))
t2 = threading.Thread(target = run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
#所以我们用try...finally来确保锁一定会被释放。
#锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，
#首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，
#效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，
#并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，
#只能靠操作系统强制终止。