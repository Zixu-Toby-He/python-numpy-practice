# python-numpy-practice

NumPy 练习与测试项目，涵盖了数组创建、随机数生成、索引操作、增删改查、矩阵运算及统计函数等常见功能。项目通过多个分模块进行练习，并配有可视化分布图（随机模块）和详细的打印输出，适合 NumPy 入门学习与复习。

## 项目结构

```
python-numpy-practice/
├── .gitignore
├── LICENSE
├── README.md
├── numpy综合练习.py                     # 主入口，依次运行所有分测试模块
└── 【练习测试】numpy/
    └── 分测试/
        ├── __init__.py                  # 包初始化，导入所有测试模块
        ├── 辅助.py                      # 辅助函数（nextline, pause, printshift）
        ├── 随机测试.py                  # 随机数生成与分布可视化
        ├── frombuffer测试.py            # 从字节缓冲区创建数组
        ├── empty_ones_zeros_full测试.py # 空数组、全0/全1/全填充数组
        ├── 数组索引操作.py              # 索引、切片与赋值
        ├── 数组增删与查询.py            # 数组合并、删除与条件查询
        ├── 矩阵操作.py                  # 矩阵对象与特殊矩阵生成
        └── 统计函数.py                  # 常用统计函数
```

## 模块说明

### 1. 随机测试 (`随机测试.py`)
- 生成均匀分布 (`numpy.random.rand`)
- 生成标准正态分布 (`numpy.random.randn`)
- 生成整数随机数 (`numpy.random.randint`)
- 生成指定均值/方差的正态分布 (`numpy.random.normal`)
- 使用 `matplotlib` 绘制概率密度分布图和累积分布图

### 2. frombuffer 测试 (`frombuffer测试.py`)
- 将字符串按不同编码 (`utf-8` / `utf-16` / `utf-32`) 转换为字节数组
- 使用 `numpy.frombuffer` 将其转换为不同数据类型的数组

### 3. 空数组、全0/全1/全填充 (`empty_ones_zeros_full测试.py`)
- `numpy.empty` / `numpy.zeros` / `numpy.ones` / `numpy.full`
- 对应的 `_like` 系列函数，依据已有数组形状创建新数组

### 4. 数组索引操作 (`数组索引操作.py`)
- 基本索引：`arr[0]`, `arr[0][1]`, `arr[1,2]`
- 切片：`arr[0][:3]`, `arr[2:8,1:4]` 等
- 下标赋值：单个元素赋值、整行/列赋值、子区域赋值

### 5. 数组增删与查询 (`数组增删与查询.py`)
- 横向合并 `hstack` / 纵向合并 `vstack`
- 行列删除 `numpy.delete`
- 条件查询 `numpy.where`，包括返回值用于布尔索引

### 6. 矩阵操作 (`矩阵操作.py`)
- 创建 `numpy.matrix` 对象
- 特殊矩阵：单位矩阵 (`eye`)、对角矩阵 (`diag`)
- 矩阵加减、乘法、求逆

### 7. 统计函数 (`统计函数.py`)
- 求和、均值、加权平均、中位数
- 最小/最大值及其索引
- 极差、方差、标准差
- 累加和 (`cumsum`)

## 运行方式

1. 克隆本仓库或下载所有文件
2. 安装依赖：
   ```bash
   pip install numpy matplotlib
   ```
3. 进入项目根目录，运行主程序：
   ```bash
   python numpy综合练习.py
   ```
   - 程序会按模块依次执行，每完成一个模块会暂停，按任意键继续。
   - 随机测试模块会弹出 matplotlib 窗口展示分布图，关闭窗口后程序继续。

   也可单独运行某个模块，例如：
   ```bash
   python "【练习测试】numpy/分测试/矩阵操作.py"
   ```

## 环境要求

- Python 3.7+
- numpy
- matplotlib

## 许可证

本项目采用 [MIT License](LICENSE)，版权 © 2026 Zixu-Toby-He。

---

**注意**：项目路径中包含中文字符，在 Linux/macOS 系统下运行请确保终端编码支持中文，或可自行重命名文件夹。代码中部分字符串为中英混合，适用于学习场景，不影响逻辑执行。