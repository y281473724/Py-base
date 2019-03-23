from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
	print('Run child Process %s (%s)...' %(name,os.getpid()))
#getpid()方法返回当前进程的id

if __name__=='__main__':
	print('Parent process %s.'%os.getpid())
	#创建一个Process实例，用start方法启动
	p = Process(target = run_proc, args = ('test',))
	#target：要执行函数； args：函数的参数
	print('Child process will start.')
	p.start()
	p.join()#该方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print("Child process end.")