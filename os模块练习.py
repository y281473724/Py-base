#在指定的盘符或目录中按输入的字符查找文件或文件夹。
import os,sys, logging


def searchDesignStr(Spath,st):
	try:
		lt = os.listdir(Spath)
		abslt = []
		for x in lt:
			abslt.append(os.path.join(Spath, x))
		for y in abslt:
			if os.path.isfile(y):
				if st in os.path.split(y)[1]:
#				print(os.path.split(y)[1])#打印文件名称的相对路径
					print(y)#打印文件的绝对路径
			else:
				searchDesignStr(y,st)
	except PermissionError as e:
		logging.exception(e)

def searchDesignDir(Spath,st):
	try:
		lt = os.listdir(Spath)
		abslt = []
		for x in lt:
			abslt.append(os.path.join(Spath, x))
		for y in abslt:
			if os.path.isdir(y):
				if st in y:
					print(y)
				searchDesignStr(y,st)
	except PermissionError as e:
		logging.exception(e)

def main():

	menu = input("""请选择查询方式：
        1.盘符查询（例如:  C、D、E...）
        2.路径查询（例如:  E:\\program\\download....）
        3.退出
        """)
	menu1 = input("""请选择查询类型：
        1.文件夹
        2.文件
        3.退出
        """)
	
	if menu == '1':
		P = input("输入想要查询的盘符：")
		local_path = "{}:\\".format(P)
	elif menu == '2':
		P = input("输入想要查询的路径：")
		local_path = P
	elif menu == '3':
		sys.exit()
	else:
		print("无效的指令")
	s = input('请输入想要查询的字符：')
	if menu1 == '1':
		searchDesignDir(local_path,s)
	elif menu1 == '2':
		searchDesignStr(local_path,s)
	elif menu1 == '3':
		sys.exit()
	else:
		print("无效的指令")

main()
input("请输入任意键退出")
