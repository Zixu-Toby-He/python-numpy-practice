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
	print("numpy.empty(shape,dtype)可以生成一组未经过初始化的数组")
	code = "numpy.empty(shape=(3,5),dtype=\"double\")"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	nextline()

	print("numpy.full(shape,fill_value,dtype)可以生成值全部为fill_value的数组")
	code = "numpy.full(shape=(3,5),fill_value = 1.5,dtype=\"double\")"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	nextline()

	print("numpy.ones 和 numpy.zeros 为 numpy.full在 fill_value = 0和1 的特殊情况")
	code = "numpy.zeros(shape=6,dtype=\"double\")"
	print("\t{} -> {}".format(code,repr(eval(code))))
	code = "numpy.ones(shape=6,dtype=\"double\")"
	print("\t{} -> {}".format(code,repr(eval(code))))
	nextline()

	print("这些函数均具有对应的 like 形式，其功能在于通过给定数组的形状来决定新数组的形状")
	print("数组原型 = [[1,2,3,4,5],[6,7,8,9,10]]")
	数组原型 = [[1,2,3,4,5],[6,7,8,9,10]]
	code = "numpy.empty_like(数组原型,dtype=\"int\")"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "numpy.full_like(数组原型,fill_value=5,dtype=\"int\")"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "numpy.zeros_like(数组原型,dtype=\"int\")"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "numpy.ones_like(数组原型,dtype=\"int\")"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	nextline()

if __name__=="__main__":
	main()
	pause()