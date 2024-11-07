# Things to learn for new students in the Lab for AI Chips and Systems of BJTU <br> 智能芯片与应用实验室新生学习指南

* 注意：新生一定认真学习相关基础知识，特别是标记了推荐的内容，至少看两遍
* 要多动手，通过练习才能掌握
* 要主动，不懂就问

# Basic Engineering Skills You Have to Master <br> 硕士生根据个人研究方向学习以下内容

## Software Programming

Learn the following two programing langrages

* C/C++ (C99/C++11)
* Python (v3.0)

Do the following projects to practice and learn good habits when programming in C

* [codewithc](https://www.codewithc.com/c-projects-with-source-code/)
* [一个python教程](https://github.com/overmind1980/oeasy-python-tutorial)

Here's another good repo that has lots of good projects for you to practice.

* [Project-Based-Tutorials-in-C](https://github.com/rby90/Project-Based-Tutorials-in-C) (try 'Emulator 101', 'hash table', 'How to Write a Video Player in Less Than 1000 Lines')

Learn the following Good Coding Styles and use them in your research projects:

* [C语言的语法风格与代码书写规范指南](https://www.ctolib.com/topics-55863.html) （简单）
* [NASA C coding style](http://mechatronics.me.wisc.edu/labresources/DataSheets/NASA-GSFC_C_Programming_Styles-94-003.pdf), NASA, 1994 （推荐）
* [Recommended C Style and Coding Standards](https://www.maultech.com/chrislott/resources/cstyle/indhill-cstyle.pdf), UC Berkeley, 1997 （简单）
* [Guidelines for the use of the C language in critical systems](http://caxapa.ru/thumbs/468328/misra-c-2004.pdf), MISRA, 2018 （高级）
* [A list of C and C++ Style Guides](https://www.maultech.com/chrislott/resources/cstyle/)
* [Embedded C programming](http://www.eng.auburn.edu/~nelson/courses/elec3040_3050/C%20programming%20for%20embedded%20system%20applications.pdf)

Some other good projects based on C/C++

* [Darknet: Open Source Neural Networks in C](https://pjreddie.com/darknet/)（深度学习最好的学习C/C++开发实例，推荐）
* [BM3D denoising algorithm](https://github.com/20logTom/BM3D)
* [ARM Compute Library](https://github.com/ARM-software/ComputeLibrary)

Software Optimizations on Different Platforms

*[软件代码优化资源](https://agner.org/optimize/)（推荐学习）

## Deep Learning Frameworks

* [一个韩国人的教程很简洁](https://github.com/yunjey/pytorch-tutorial)（入门推荐）
* [动手学深度学习PyTorch版](https://github.com/ShusenTang/Dive-into-DL-PyTorch)（入门推荐）
* Pytorch[中文教程](https://github.com/zergtant/pytorch-handbook)
* Nvidia官方training、inference[例子、参考代码](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Classification/ConvNets)
* [Deep-Learning-with-PyTorch-Chinese 中文翻译含例程](https://github.com/ShusenTang/Deep-Learning-with-PyTorch-Chinese)
* [斯坦福李飞飞老师课程 Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/index.html)（做目标检测同学推荐学习）


#### Excellent Deeplearning Project Using Pytorch

There are many good examples that we have collected from github, and students can learn how to write "good" pytorch codes by reading and modifying the codes from these example project. A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/project/project.md).

#### How to setup the GPU and Pytorch environment

[Pytorch安装说明](https://github.com/doonny/basic_knowledge/blob/master/project/install.md)

#### 目标检测框架mm-detection代码讲解

* [代码构建一](https://zhuanlan.zhihu.com/p/337375549), [代码构建二](https://zhuanlan.zhihu.com/p/341954021)
* [一些代码注释](https://github.com/ming71/mmdetection-annotated)

## Hardware Basic Knowledge

Read the following two books to learn basic concepts for digital circuit design and computer architecture. 

### Digital Circuit/Logic Design
Important concepts to understand include **combinatonal logic and sequential logic (组合逻辑和时序逻辑), register寄存器(Flip-Flop circuit), FSM状态机, counter计数器, decoder/encoder编码器和译码器, FIFO, RAM, etc.** Read the following two books:

* ''数字逻辑设计与计算机组成, 戴志涛等，机械工业出版社''
* ["Digital Logic"](https://inst.eecs.berkeley.edu/~cs150/archives.html)

### Computer Architecture
Important concepts to understand include **pipeline, memory hierarchy, roofline model, Amdahl's law, ILP (instruction level parallelism), TLP (task level parallelism), DLP (data level parallelism), SIMD/VLIW processor, etc.** Read the following two books:

* [''Computer Organization and Design The Hardware Software Interface''](http://staff.ustc.edu.cn/~llxx/cod/reference_srcs.html), ARM Edition, 2017（重要，零基础学习）
* [''Computer Architecture A Quantitative Approach''](https://book.douban.com/subject/6795919/), 6th Edition, 2019 （重要，进阶学习）

More reading:

* Loop-carried dependency: [1](https://www.cs.utexas.edu/~lin/cs380c/handout27.pdf), [2](https://people.engr.ncsu.edu/efg/506/s10/www/lectures/notes/lec5.pdf)
* Roofline Model Basic: ./doc/Roofline Model.pdf
* [并行处理的几种常见方式](http://www.inf.ed.ac.uk/teaching/courses/pa/Notes/lecture02-types.pdf)（推荐）



## FPGA Design

After you have basic knowledges on digital circuit and computer architectures, you could learn FPGA design or heterogenours computing (using FPGA as accelerators). We recommand using HLS (High-level Synthesis)-based schemes (C/C++-based HLS or OpenCL) rather than RTL-level programming (i.e., Verilog and VHDL) to design application specific circuit on FPGAs (However, if you have time, you should always learn Verilog). 


Go to [HERE](https://github.com/doonny/basic_knowledge/blob/master/fpga/fpga.md) and read all the materials we have listed.

FPGA相关学习资料在[这里](https://github.com/doonny/basic_knowledge/blob/master/fpga/fpga.md) (零基础、进阶推荐必读)。

Finally, learn our opensource project [PipeCNN](https://github.com/doonny/PipeCNN). Run the examples, such as caffenet, vgg-16, resnet, YOLO on the Arria-10 FPGA and The Zynq FPGA platforms. Learn how to configure, compile, debug the source codes and profile the performance of the accelerator. After entering our lab, you will have access to our latest designs, i.e., PipeCNN-v2 and PipeCNN-sparse, which are in private repos.

Zhang DeZheng has wrote a good study note on PipeCNN, please read it [here](https://github.com/doonny/basic_knowledge/blob/master/PipeCNN_note.md).

#### A list of GOOD FPGA accelerator design can be found [here]()

## GPU Design

Learn TensorRT and CUDA programing. Try examples on our TX2/TK1 platforms.

* [TensorRT](https://developer.nvidia.com/tensorrt)



# Research Related Topics <br> 高年级硕士和博士生学习内容

First, students should read the following artichles to learn how to write research papers.

* [''How to write a great research paper''](http://www.sohu.com/a/254967611_473283), Deep Learning Indaba, Stellenbosch, 2018
* [''How to Publish a Research Paper''](https://www.wikihow.com/Publish-a-Research-Paper), wikiHow, 2019
* [''How to Write a Good Scientific Paper''](https://spie.org/samples/9781510619142.pdf), Chris A. Mack, SPIE, 2018
* [''How to Write a Good Paper in Computer Science and How Will It Be Measured by ISI Web of Knowledge''](http://univagora.ro/jour/index.php/ijccc/article/view/2493), R?zvan Andonie, et.al., 2010

Secondly, read the following selected papers in each research topics, which are really good examples in the related fields.


### Tutorials for Hardware Architectures for DNN

Students who are working on hardware designs for deep neural networks should read the following tutorials.

* [Hardware Architectures for Deep Neural Networks](http://eyeriss.mit.edu/tutorial.html), MICRO Tutorial 2016. （推荐）

### FPGA Accelerator Design

* Optimizing FPGA-based Accelerator Design for Deep Convolutional Neural Networks, FPGA 2015.
* Throughput-Optimized OpenCL-based FPGA Accelerator for Large-Scale Convolutional Neural Networks, FPGA 2016.
* An OpenCL Deep Learning Accelerator on Arria 10, FPGA 2017.
* Improving the Performance of OpenCL-based FPGA Accelerator for Convolutional Neural Network, FPGA 2017.
* A Framework for Generating High Throughput CNN Implementations on FPGAs, FPGA 2018.
* An Efficient Hardware Accelerator for Sparse Convolutional Neural Networks on FPGAs, FCCM 2019.

The following survery papers are also worth reading.

* A Survey of FPGA Based Neural Network Accelerator, ACM TRETS 2017.
* Deep Neural Network Approximation for Custom Hardware: Where We’ve Been, Where We’re Going, ACM Computing Surveys 2019.

Our own research papers on FPGA accelerators:

* PipeCNN: An OpenCL-Based Open-Source FPGA Accelerator for Convolution Neural Networks, FPT 2017
* ABM-SpConv: A Novel Approach to FPGA-Based Acceleration of Convolutional Neural Network Inference, DAC 2019


A more complete paper list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/fpga.md).


#### Sparse Convolution Design


A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/sparse.md).


### Neural network optimization (quantization, pruning, et.al.)

#### Neural Network Quantization

* Ristretto: A Framework for Empirical Study of Resource-Efficient Inference in Convolutional Neural Networks, IEEE T-NNLS 2018.
* 8-bit Inference with TensorRT, Nvidia 2017.
* Quantizing deep convolutional networks for efficient inference: A whitepaper, Google, 2018.

A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/quantization.md).

#### Network Pruning and Compression

A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/pruning.md).

#### Neural Architecture Search (NAS)

A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/NAS.md).

#### Object Detection

A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/object_detection.md).
