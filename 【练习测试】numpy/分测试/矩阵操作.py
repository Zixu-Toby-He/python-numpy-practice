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
	print("除了 numpy.ndarray 以外 numpy 还提供了 numpy.matrix 专门作为矩阵对象，该对象仅支持二维数组")
	print("numpy.matrix 对象通过 numpy.mat 函数创建")
	code = "numpy.mat([[1,2,3,4,5],[6,7,8,9,10]])"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "numpy.mat(numpy.zeros(shape=(5,4)))"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	nextline()

	print("由于 numpy 版本的更新，以下函数返回值均被修改为 numpy.array 类型，但仍然可以通过转化得到相应的矩阵")
	nextline()
	print("特殊矩阵的生成")
	print("\t利用 numpy.eye(N=行数, M=列数/无, k=偏移, dtype, ...) 可以生成归一化矩阵")
	code = "numpy.eye(5)"
	print("\t\t{} -> 以下".format(code))
	printshift(eval(code),3)
	code = "numpy.eye(5,4)"
	print("\t\t{} -> 以下".format(code))
	printshift(eval(code),3)
	code = "numpy.eye(M=10,N=10,k=3)"
	print("\t\t{} -> 以下".format(code))
	printshift(eval(code),3)
	print("\t利用 numpy.diag(v=对角元素数组,k=偏移) 生成对角矩阵")
	code = "numpy.diag([1,2,3,4,5])"
	print("\t\t{} -> 以下".format(code))
	printshift(eval(code),3)
	code = "numpy.diag([1,2,3],k=2)"
	print("\t\t{} -> 以下".format(code))
	printshift(eval(code),3)
	nextline()

	print("矩阵对象遵循的计算法则与数学上的矩阵运算相对应")
	矩阵a = numpy.mat([[1,2],[3,4]])
	矩阵b = numpy.mat([[5,6],[7,8]])
	print("矩阵a -> 如下")
	printshift(矩阵a,1)
	print("矩阵b -> 如下")
	printshift(矩阵b,1)
	code = "矩阵a + 矩阵b"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "矩阵a - 矩阵b"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "矩阵a * 矩阵b"
	print("\t{} -> 以下".format(code))
	printshift(eval(code),2)
	code = "矩阵a.I "
	print("\t{} （求逆矩阵）-> 以下".format(code))
	printshift(eval(code),2)
	nextline()



if __name__=="__main__":
	main()
	pause()