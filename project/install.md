# caffe、CUDA、pytorch安装

## Caffe
官方参考http://caffe.berkeleyvision.org/install_apt.html，
系统要求Ubuntu 14.04、16.04

1）依赖项
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev （14.04依赖项）
其中OpenCV也可通过source手动安装并配置
安装Linux Header文件
$ sudo apt-get install linux-headers-$(uname -r)

2）BLAS
install ATLAS by sudo apt-get install libatlas-base-dev or install OpenBLAS by sudo apt-get install libopenblas-dev or MKL for better CPU performance.

3）CUDA
CUDA版本与driver版本关系（https://docs.nvidia.com/deploy/cuda-compatibility/index.html）


## GPU显卡驱动安装

- 通过ppa安装（推荐）
```
sudo apt-get purge nvidia-*
sudo add-apt-repository ppa:graphics-drivers/ppa and then sudo apt-get update.
sudo apt-get install software-properties-common（可选）
sudo apt-get install nvidia-375（这里选择你需要的版本号）
```
然后重启机器，执行nvidia-smi查看显卡信息 （装完cuda还也要重启）

## 安装CUDA（最新CUDA9/10可以不需要进行a、b步骤）：
a）ctrl + alt + f1 进入tty1界面

b）关闭x桌面服务
sudo service lightdm stop

c）安装依赖库
sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev 

d）安装CUDA
sudo sh cuda_8.0.61_375.26_linux.run --no-opengl-libs 
如果有PATCH可以把PATCH也安装好。

e）添加环境变量
export CUDA_HOME=/usr/local/cuda 
export PATH=$PATH:$CUDA_HOME/bin 
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64$LD_LIBRARY_PATH

f）进入example中Utility，编译deviceQuery例子，运行，如果PASS证明安装完成。

## 安装cuDNN

参考https://developer.nvidia.com/cudnn注册并下载对应版本

a）解压压缩文件到特定路径

b）添加路径
export LD_LIBRARY_PATH=/your path to cudnn/lib64:$LD_LIBRARY_PATH

c）拷贝cudnn.h文件到cuda目录下
拷贝lib下文件到cuda/lib64目录下，注意增加读权限

## 安装nccl（pytorch自带nccl后端，可以不需要自己装）

- 方法一 用源文件安装：

a）版本v1.2.3-1+cuda8.0
下载 https://github.com/NVIDIA/nccl/tree/v1.2.3-1+cuda8.0

b）编译和测试
make CUDA_HOME=<cuda install path> test
测试：./build/test/single/all_reduce_test 1000000

c）安装
sudo make install（默认都安装到/usr/local下了）
记住要sudo ldconfig一下更新缓存

- 方法二 用deb安装（推荐）：

下载deb安装文件，如nccl-repo-ubuntu1804-2.4.8-ga-cuda10.0_1-1_amd64.deb
```
dpky -i nccl-repo-ubuntu1804-2.4.8-ga-cuda10.0_1-1_amd64.deb
sudo apt update
sudo apt install libnccl2 libnccl-dev
```
如果要指定某个版本：
sudo apt install libnccl2=2.0.0-1+cuda8.0 libnccl-dev=2.0.0-1+cuda8.0

## 安装Conda和Pytorch

a）https://repo.continuum.io/archive/ 下载需要的版本

b）安装
bash Anaconda2-5.1.0-Linux-x86_64.sh

c）添加PATH

d）安装Pytorch和torchvision
conda install pytorch=1.0 torchvision cudatoolkit=10.0

e）测试，进入python，然后
```
import torch
import torchvision
print(torch.cuda.is_available())
```
或者
```
import torch
x=torch.Tensor(5,3)
print x
```

f）卸载
conda uninstall pytorch torchvision

g) 如果使用lmdb数据库还需要安装：
conda install -c conda-forge python-lmdb

- 问题处理：

1）切换国内源：
```
vim .condarc
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
show_channel_urls: true
```

2）多环境管理：
查看当前conda所有可用环境
conda info -e
创建一个新环境
conda create -n py36 python=3.6
切换到想要的环境
source activate py36
退出当前环境
source deactivate

## 安装 DALI

安装：
pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/cuda/10.0 nvidia-dali

升级：待补充

## 安装 APEX

待补充


## 安装 Caffe

a）下载源码
git clone https://github.com/BVLC/caffe.git

b）其他依赖库：
sudo apt install libboost-python-dev python-skimage python-protobuf

c）编译配置
由于conda自带库和caffe不兼容，编译前先屏蔽conda相关库和路径

 - 方法一通过Cmake编译（推荐，提示信息更清楚）：

修改CMakeLists.txt选择相关编译项，如：
USE_NCCL -> ON
然后
```
mkdir build
cd build
cmake ..
make all
make install
make runtest
```

 - 方法二直接Makefile编译：

将 Makefile.config.example 文件复制一份并更名为 Makefile.config
修改相关编译项如：

USE_CUDNN := 1

注意选择用conda的python还是系统python

USE_NCCL := 1

修改Makefile，增加
NVCCFLAGS += -D_FORCE_INLINES -ccbin=$(CXX) -Xcompiler -fPIC $(COMMON_FLAGS)

如果提示找不到hdf5，增加hdf5支持：
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include  
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu （14.04直接这个目录下，https://packages.ubuntu.com/trusty/amd64/libhdf5-dev/filelist）

如果是16.04修改为：
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include /usr/include/hdf5/serial/ LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu/hdf5/serial
（或者/your conda path/lib 待验证）

c）编译
```
make all -j8
make pycaffe
make runtest -j8
```
如果 make runtest -j8 时找不到libhdf5相关库，增加下面路径（make all之前不能加，否则anaconda中有些lib会和系统lib冲突）：
export LD_LIBRARY_PATH=/your conda path/lib:/usr/local/lib:$LD_LIBRARY_PATH

d）添加Python路径

export PYTHONPATH=/path/to/caffe/python:$PYTHONPATH

7）为Conda的Python安装依赖项
conda install -c conda-forge python-lmdb
conda install protobuf

问题处理：
1）CUDA9以上可能会出现cublas库不识别的问题，需要卸载老版本cmake，安装新版本，如3.14.7版本，参考：https://www.linuxidc.com/Linux/2018-09/154165.htm


## 常用命令
nvidia-smi topo --matrix
nvidia-smi dmon
nvidia-smi pmon

## 参考评测文章：
（1）https://www.pugetsystems.com/labs/hpc/PCIe-X16-vs-X8-with-4-x-Titan-V-GPUs-for-Machine-Learning-1167/

（2）