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
def 显示分布(函数, 数据范围: tuple[int,int] = None, 精细度:int = 10, 数据量:int = 1000):
	if 数据范围==None:
		数据范围 = (0,1)
	下限,上限 = 数据范围
	随机生成 = 函数(数据量)
	分段 = numpy.linspace(下限,上限,精细度+1)
	段中点 = (分段[1:]+分段[:-1])/2
	分布 = numpy.empty(精细度)
	累计 = numpy.empty(精细度+1)
	for i in range(精细度+1):
		累计[i] = numpy.sum(随机生成 <= 分段[i])/数据量
	分布 = (累计[1:] - 累计[:-1]) / (分段[1:] - 分段[:-1])
	matplotlib.pyplot.figure(figsize=(14,6))
	分布图 = matplotlib.pyplot.subplot(1,2,1)
	累计图 = matplotlib.pyplot.subplot(1,2,2)
	长度 = 上限-下限
	绘图下限 = 下限 - 0.1*长度
	绘图上限 = 上限 + 0.1*长度
	分布图.plot(段中点,分布)
	分布图.scatter(段中点,分布)
	分布图.set_ylabel("p")
	分布图.set_ybound(0, 1.2*numpy.max(分布))
	分布图.grid()
	#分布图.set_xbound(绘图下限,绘图上限)
	累计图.plot(分段,累计)
	累计图.scatter(分段,累计)
	累计图.set_ylabel("$P(X<x)$")
	累计图.set_ybound(0,1.1)
	累计图.set_xbound(绘图下限,绘图上限)
	累计图.grid()
	matplotlib.pyplot.show()

def main():
	print("利用 random 模块生成随机数组")
	nextline()

	print("\tnumpy.random.rand：生成 0~1 之间的随机数组（均匀分布）")
	print("\t参数列表：numpy.random.rand(d1,d2,d3...)，用于决定生成数组的维度信息")
	数值 = numpy.random.rand()
	print("\t\tnumpy.random.rand()    -> 数值：{}，类型：{}".format(数值,type(数值)))
	print("\t\tnumpy.random.rand(3)   -> {}".format(repr(numpy.random.rand(3))))
	print("\t\tnumpy.random.rand(3,5) -> 如下")
	printshift(numpy.random.rand(3,5),2)
	nextline()
	显示分布(numpy.random.rand, 数据范围=(0,1), 数据量 = 10000)

	print("\tnumpy.random.randn：按照标准正态分布（N(mu=0,sigma=1) = 1/sqrt(2*pi) * e^{-1/2*x^2}）生成随机数组")
	print("\t参数列表：numpy.random.randn(d1,d2,d3...)，用于决定生成数组的维度信息")
	print()
	数值 = numpy.random.randn()
	print("\t\tnumpy.random.randn()    -> 数值：{}，类型：{}".format(数值,type(数值)))
	print("\t\tnumpy.random.randn(3)   -> {}".format(repr(numpy.random.randn(3))))
	print("\t\tnumpy.random.randn(3,5) -> 如下")
	printshift(numpy.random.randn(3,5),2)
	nextline()
	显示分布(numpy.random.randn, 数据范围=(-5,5), 精细度=30, 数据量 = 100000)

	print("\tnumpy.random.randint：生成整数随机数")
	print("\t参数列表：numpy.random.randn(low,high=None,size=None)")
	print("\t\t其中 high=None 时输出 0~low 之间的整数随机数")
	数值 = numpy.random.randint(10)
	print("\t\tnumpy.random.randint(10)                         -> 数值：{}，类型：{} （0~3之间）".format(数值,type(数值)))
	print("\t\tnumpy.random.randint(10,20)                      -> {}".format(numpy.random.randint(1,5)))
	print("\t\tnumpy.random.randint(low=10,high=50,size=5)      -> {}".format(repr(numpy.random.randint(low=10,high=50,size=5))))
	print("\t\tnumpy.random.randint(low=10,high=50,size=(3,5))  -> 如下")
	printshift(numpy.random.randint(low=10,high=50,size=(3,5)),2)
	nextline()
	显示分布(lambda x:numpy.random.randint(low=0, high=10, size=x), 数据范围=(0,10), 精细度=10)

	print("\tnumpy.random.normal：按照正态分布（N(mu,sigma) = 1/(sqrt(2*pi)*sigma) * e^{- (x-mu)^2/(2*sigma^2)}）生成随机数组")
	print("\t参数列表：numpy.random.normal(loc=0.0,scale=1.0,size=None)，")
	print("其中 loc = mu = 均值，scale = sigma = 方差，size决定生成数组的维度信息")
	print("取mu = 5, sigma = 1.2")
	均值 = 5
	方差 = 1.2
	数值 = numpy.random.normal(loc=5,scale=1.2)
	print("\t\tnumpy.random.normal(5, 1.2)                     -> 数值：{}，类型：{}".format(数值,type(数值)))
	print("\t\tnumpy.random.normal(5, 1.2, size=3)             -> {}".format(repr(numpy.random.normal(loc=5,scale=1.2,size=3))))
	print("\t\tnumpy.random.normal(loc=5,scale=1.2,size=(3,5)) -> 如下")
	printshift(numpy.random.normal(loc=5,scale=1.2,size=(3,5)),2)
	nextline()
	显示分布(lambda x:numpy.random.normal(均值,方差,x), 数据范围=(均值-4*方差,均值+4*方差), 精细度=60, 数据量 = 600000)

if __name__=="__main__":
	main()
	pause()