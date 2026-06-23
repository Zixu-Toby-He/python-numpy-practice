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
	数组样例 = numpy.arange(20).reshape((4,5))
	print("数组样例：")
	printshift(数组样例,1)
	nextline()

	print("数组的合并")
	待合并的数组 = numpy.arange(100,120).reshape((4,5))
	print("\t待合并的数组")
	printshift(待合并的数组,2)
	nextline()
	print("\t利用 numpy.hstack 横向合并")
	print("\tnumpy.hstack((数组样例,待合并的数组),dtype = \"float32\") -> 以下")
	printshift(numpy.hstack((数组样例,待合并的数组),dtype = "float32"),2)
	print("\t利用 numpy.vstack 纵向合并")
	print("\tnumpy.vstack((数组样例,待合并的数组),dtype = \"double\") -> 以下")
	printshift(numpy.vstack((数组样例,待合并的数组),dtype = "double"),2)

	print("数组行与列的删除")
	print("利用 numpy.delete 函数可以做到对函数行与列的删除")
	print("参数列表：")
	print("\tnumpy.delete(原数组, 需要删除的行列编号（可以是组合）, axis = 行或列)")
	print("\tnumpy.delete(数组样例, 2, axis = 1) -> 以下")
	printshift(numpy.delete(数组样例, 2, axis = 1),2)
	print("\tnumpy.delete(数组样例, (1,2), axis = 0) -> 以下")
	printshift(numpy.delete(数组样例, (1,2), axis = 0),2)
	nextline()

	print("数组的查询")
	print("\t利用 numpy.where 函数可以查询数组数组内对应元素，也可以按照对应行列生成需要的数组")
	print("\tnumpy.where(数组样例 > 5) -> 以下")
	printshift(numpy.where(数组样例 > 5),2)
	print("\tnumpy.where(数组样例 > 5, 3, -2) -> 以下")
	printshift(numpy.where(数组样例 > 5, 3, -2),2)
	print("\tnumpy.where 函数的返回值还可以直接用到下标上去对元素做筛选，生成一个一维数组")
	printshift(数组样例[numpy.where((数组样例%4)<2)],2)


if __name__=="__main__":
	main()
	pause()