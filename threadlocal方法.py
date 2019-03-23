
import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
	#获取当前线程关联的student：
	std = local_school.student
	print('Hello, %s (in %s)' %(std, threading.current_thread().name))

def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread,args = ('Alice',),name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
#全局变量local_school就是一个ThreadLoacal对象，
#每个Thread对它都可以读写student属性，但互不影响。
#可以把local_school看作全局变量，但每个属性如local_school.student都是线程的局部变量
#可以任意读写而互补干扰，也无需管理锁的问题，ThreadLocal内部会处理
#可以理解全局变量local_school是一个dict，不但可以用local_school.student，
#还可以绑定其他变量，如local_school.teacher等等
#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。