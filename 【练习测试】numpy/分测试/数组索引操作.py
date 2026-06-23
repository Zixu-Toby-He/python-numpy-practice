import numpy
import matplotlib.pyplot
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
	数组样例 = (numpy.arange(100)).reshape((10,10))
	print("\t数组样例:")
	printshift(数组样例,2)
	nextline()

	print("一般下标操作：")
	print("\t数组样例[0]    -> {}".format(repr(数组样例[0]   )))
	print("\t数组样例[0][1] -> {}".format(repr(数组样例[0][1])))
	print("\t数组样例[1,2]  -> {}".format(repr(数组样例[1,2] )))
	nextline()

	print("下标切片")
	print("\t数组样例[0][:3]     -> {}".format(repr(数组样例[0][:3]    )))
	print("\t数组样例[0][3:8]    -> {}".format(repr(数组样例[0][3:8]   )))
	print("\t数组样例[1][::-1]   -> {}".format(repr(数组样例[1][::-1]  )))
	print("\t数组样例[1][7:2:-1] -> {}".format(repr(数组样例[1][7:2:-1])))
	nextline()
	print("\t数组样例[2:8][1:4]  -> 以下（先计算数组样例[2:8]得到6*10的数组，在对这个6*10的数组进行切片）")
	printshift(数组样例[2:8][1:4], 2)
	print("\t数组样例[2:8,1:4]  -> 以下（正常切片）")
	printshift(数组样例[2:8,1:4], 2)
	print("\t数组样例[(1,3,5),(2,4,6,8,0)]  -> 以下")
	try:
		printshift(数组样例[((1,3,5),(2,4,6,8,0))], 2)
	except IndexError as e:
		import traceback
		printshift(traceback.format_exc(), 2)
	nextline()

	nextline()

	print("根据下标赋值")
	print("赋值样例 = 数组样例.copy()")
	赋值样例 = 数组样例.copy()
	nextline()

	print("\t赋值样例[9,9] = 0 -> 如下")
	赋值样例[9,9] = 0
	printshift(赋值样例,2)
	nextline()

	print("\t赋值样例[1,1:5] = range(2,6) -> 如下")
	赋值样例[1,1:5] = range(2,6)
	printshift(赋值样例,2)
	nextline()

	print("\t赋值样例[2:7,2:7] = numpy.arange(25).reshape(shape=(5,5)) -> 如下")
	赋值样例[2:7,2:7] = numpy.arange(25).reshape((5,5))
	printshift(赋值样例,2)
	nextline()

	nextline()



if __name__=="__main__":
	main()
	pause()