import numpy
import os

def nextline():
	print("")
def pause():
	nextline()
	os.system("pause")
def printshift(obj,n: int):
	间隔 = "\t" * n
	分行 = "\n" + 间隔
	if(not(isinstance(obj,str))):
		obj = repr(obj)
	print(间隔 + 分行.join(obj.split("\n")))

def main():
	print("numpy.frombuffer(buffer,dtype=float,count=-1,offset=0)")
	print("\t该函数可以将字符串编码对象转化为数组")
	nextline()

	字符串 = "Hello world! 你好世界！"
	代码模板 = "numpy.frombuffer(\"{}.\".encode(encoding = \"{}\"),dtype=\"{}\")"

	code = 代码模板.format(字符串,"utf-8","int8")
	print("\t{} -> 如下".format(code))
	printshift(eval(code),2)
	nextline()

	code = 代码模板.format(字符串,"utf-16","int16")
	print("\t{} -> 如下".format(code))
	printshift(eval(code),2)
	nextline()

	code = 代码模板.format(字符串,"utf-32","int32")
	print("\t{} -> 如下".format(code))
	printshift(eval(code),2)
	nextline()


if __name__=="__main__":
	main()
	pause()