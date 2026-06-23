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
	print("numpy 提供用于统计的函数")
	数组样例 = numpy.random.randint(low = 0, high = 10, size = 100)
	print("数组样例：")
	printshift(数组样例,1)
	nextline()

	code = "numpy.sum(数组样例)"
	print("{:50s} -> {}".format(code,eval(code)))
	code = "numpy.mean(数组样例)"
	print("{:<50s} -> {}".format(code,eval(code)))
	code = "numpy.average(数组样例)"
	print("{:<50s} -> {}".format(code,eval(code)))
	code = "numpy.average(数组样例, weights = range(1,101))"
	print("{:<50s} -> {}".format(code,eval(code)))
	code = "numpy.median(数组样例)"
	print("{:<50s} -> {}".format(code,eval(code)))
	nextline()
	
	code = "(numpy.argmin(数组样例), numpy.min(数组样例))"
	print("{:<40s} （minIndex,min）-> {}".format(code,eval(code)))
	code = "(numpy.argmax(数组样例), numpy.max(数组样例))"
	print("{:<40s} （maxIndex,max）-> {}".format(code,eval(code)))
	nextline()

	code = "numpy.ptp(数组样例)"
	print("{:<20s} 极差   -> {}".format(code,eval(code)))
	code = "numpy.var(数组样例)"
	print("{:<20s} 方差   -> {}".format(code,eval(code)))
	code = "numpy.std(数组样例)"
	print("{:<20s} 标准差 -> {}".format(code,eval(code)))
	nextline()

	code = "numpy.cumsum(数组样例)"
	print("{} （累加）-> 以下".format(code))
	printshift(eval(code),1)
#	print("累加还可以通过 数组.cumprod 属性实现")
#	code += " == 数组样例.cumprod"
#	code = "数组样例.cumprod()"
#	print("{} -> {}".format(code,eval(code)))


if __name__=="__main__":
	main()
	pause()