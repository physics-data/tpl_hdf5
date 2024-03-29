# 芃芃快乐矩阵（HDF5）

## 问题背景

芃芃太快乐了，这次就不编故事了。

## 问题描述

你需要编写一个 Python 程序完成 HDF5 文件的输入和输出，对数据进行一个矩阵的转置。具体来说，你需要修改项目中的 `hdf5.py`，并完成以下功能：

1. 找到打开的 HDF5 文件（路径为sys.argv[1]）中 "/PPHappy" 的组下面 "PPMatrix" 的数据集，转化为 numpy 中的矩阵格式
2. 使用 numpy 提供的矩阵转置，然后把转置后的矩阵写入文件（路径为sys.argv[2]）

项目中的 `hdf5.py` 已经提供了必要的代码和提示，已经提供了部分输入和输出的代码以供参考。和之前的题目一样，可以通过执行 `python3 hd5.py [input_file] [output_file]` 来进行数据的处理，但注意不要把 `data` 目录下的文件覆盖。

## 环境准备

这次需要两个库： `h5py` 和 `numpy` 。和 `numpy` 类似，你可以用类似的方法安装 `h5py` 。

如果使用的是 WSL 或者是 Linux 可以通过这个命令安装：

```
sudo apt install python3-h5py
```

如果是用的是 macOS 系统，可以通过这个命令安装：

```
pip3 install h5py
# or
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple h5py
```

## 样例与评分

我们在 `data` 目录下提供了五组数据，分别对应不同的情况和数据量大小，这次正式评测不会使用额外的数据。和之前的题目一样，你可以通过 `python3 grade.py` 来进行一次的本地测评。

评测程序会读取你的程序输出的 HDF5 文件中相应的数据，与正确答案进行对比。

这次数据量很小，虽然仍然设置了 2s 的时间限制，但基本不会达到。

最终分数构成为：

* 黑盒 80 分：共 5 个测例，每个 16 分
* 白盒 20 分：代码风格与 Git 使用 20 分（包括恰当注释、合理命名、提交日志等）

助教以 deadline 前 GitHub 上最后一次提交为准进行评测。

## 提醒和注意事项

1. 你可以尝试运行 `h5dump data/hdf5_1.in` 查看对应的数据输入的内容，查看其它文件同理。`h5dump` 需要通过 `sudo apt install hdf5-tools` 或者 `brew install hdf5` (Homebrew) 或者 `sudo port install hdf5` (MacPorts) 安装。
2. 你也可以不采用 `numpy` 来进行矩阵的处理，但需要自己保证输出数据中数据格式和目标一致。
