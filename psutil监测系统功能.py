#psutil=process and system utilities
#psutil不仅可以通过一两行代码实现系统监控,还可以跨平台舒勇
#是系统管理员和运维工作的不可或缺的必备模块

#先来获取CPU信息:
import psutil
c = psutil.cpu_count()#CPU逻辑数量
#print(c)#输出4,说明是4核非超线程
c = psutil.cpu_count(logical = False)#CPU物理核心
#print(c)#输出2,说明是双核超线程

#统计CPU的用户/系统/空闲时间:
c = psutil.cpu_times()
#print(c)

#再实现类似top命令的CPU使用率,每秒刷新一次,累计10词
for x in range(10):
	c = psutil.cpu_percent(interval = 1, percpu = True)
#	print(c)

#使用psutil获取物理内存和交换内存信息,分别使用:
c = psutil.virtual_memory()
#print(c)
c = psutil.swap_memory()
#print(c)

#可以通过psutil获取磁盘分区/磁盘使用率和磁盘IO信息:
c = psutil.disk_partitions()#磁盘分区信息

c = psutil.disk_usage('/')#磁盘使用情况

c = psutil.disk_io_counters()#磁盘IO

#pstuil可以获取网络接口和网络连接信息
c = psutil.net_io_counters()#获取网络读写字节/包的个数

c = psutil.net_if_addrs()#获取网络接口信息

c = psutil.net_if_stats()#获取网络接口状态

#要获取当前网络连接信息,使用net_connections()
c = psutil.net_connections()

#通过pstuil可以获取到所有进程的详细信息:
c = psutil.pids()#所有进程ID

p = psutil.Process(3860)#获取指定进程ID=3860,就是chrome
print(p.name())#进程名称
print(p.exe())#进程路径
print(p.cwd())#进程工作目录
print(p.cmdline())#进程启动的命令行
print(p.ppid())#父进程的ID
print(p.parent())#父进程
print(p.children())#子进程列表
print(p.status())#进程状态
print(p.username())#进程用户名
print(p.create_time())#进程创建时间
print(p.terminal())#进程终端
print(p.cpu_times())#进程使用的CPU时间
print(p.memory_info())#进程使用的内存
print(p.open_files())#进程打开的文件
print(p.connections())#进程相关网络连接
print(p.num_threads())#进程的线程数量
print(p.threads())#所有的线程信息
print(p.environ())#进程环境变量
print(p.terminate())#进程结束


#psutil还提供了一个test()函数，可以模拟出ps命令的效果：
"""
C:\Users\Administrator>python
>>> import psutil
>>> psutil.test()
USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
SYSTEM         0    ?       ?       4 ?             09:43   07:58  System Idle Process
SYSTEM         4    ?     128     668 ?             09:43   04:52  System
DWM-1          8  1.2   54524   48088 ?             09:43   07:46  dwm.exe
SYSTEM       392    ?     364     864 ?             09:43   00:00  smss.exe
SYSTEM       456  0.8   27040   33864 ?             09:43   00:34  svchost.exe
SYSTEM       552  0.1    1332    3908 ?             09:43   00:01  csrss.exe
SYSTEM       656  0.1    1048    4476 ?             09:43   00:00  wininit.exe
.....
"""