# Things to learn for new students in Lab615

# Basic Engineering Skills You Have to Master

## Software Programming

Learn the following two programing langrages

* C (C99)
* Python (v3.0)

Do the following projects to practice and learn good habits when programming in C

* [codewithc](https://www.codewithc.com/c-projects-with-source-code/)

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

* [BM3D denoising algorithm](https://github.com/20logTom/BM3D)
* [ARM Compute Library](https://github.com/ARM-software/ComputeLibrary)

## Deep Learning Frameworks

* Pytorch[中文教程](https://github.com/zergtant/pytorch-handbook)
* [动手学深度学习PyTorch版](https://github.com/ShusenTang/Dive-into-DL-PyTorch)（入门推荐）
* Nvidia官方training、inference[例子](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Classification/ConvNets)

#### Excellent Project

There are many good examples that we have collected from github, and students can learn how to write "good" pytorch codes by reading and modifying the codes from these example project. A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/project/project.md).



## Hardware Basic Knowledge

Read the following two books to learn basic concepts for computer architecture. Important things to understand include pipeline, memory hierarchy, roofline model, Amdahl's law, ILP (instruction level parallelism), TLP (task level parallelism), DLP (data level parallelism), SIMD/VLIW processor

* [''Computer Organization and Design The Hardware Software Interface''](http://home.ustc.edu.cn/~louwenqi/reference_books_tools/Computer_Organization_and_Design_3Rd.pdf), 3rd Edition, 2004 （基础）
* [''Computer Architecture A Quantitative Approach''](https://book.douban.com/subject/6795919/), 6th Edition, 2019 （进阶）

More reading:

* Loop-carried dependency: [1](https://www.cs.utexas.edu/~lin/cs380c/handout27.pdf), [2](https://people.engr.ncsu.edu/efg/506/s10/www/lectures/notes/lec5.pdf)
* Roofline Model Basic: ./doc/Roofline Model.pdf
* [并行处理的几种常见方式](http://www.inf.ed.ac.uk/teaching/courses/pa/Notes/lecture02-types.pdf)（推荐）



## FPGA Design

Read the following book to learn OpenCL programing (GPU/FPGA):

* ''OpenCL Programming Guide'', Aaftab Munshi, et.al., 2012  [also known as The Green Book]
* [''FPGA异构计算——基于OpenCL的开发方法''](https://baike.baidu.com/item/FPGA%E5%BC%82%E6%9E%84%E8%AE%A1%E7%AE%97%E2%80%94%E2%80%94%E5%9F%BA%E4%BA%8EOpenCL%E7%9A%84%E5%BC%80%E5%8F%91%E6%96%B9%E6%B3%95), 黄乐天 等, 2015

Also, refers to Intel/Xilinx's OpenCL user guide to learn specific techniques that will be used in the project.

*  [''面向 OpenCL 的英特尔 FPGA SDK 最佳实践指南''](https://www.intel.cn/content/www/cn/zh/programmable/products/design-software/embedded-software-developers/opencl/support.html)

Finally, learn our opensource project [PipeCNN](https://github.com/doonny/PipeCNN). Run the examples, such as caffenet, vgg-16, resnet, YOLO on the DE10-nano and DE5-net platforms. Learn how to configure, compile, debug the source codes and profile the performance of the accelerator.

Zhang DeZheng has wrote a good study note on PipeCNN, please read it [here](https://github.com/doonny/basic_knowledge/blob/master/PipeCNN_note.md).


#### Information on the FPGA boards used in our lab [here](https://github.com/doonny/basic_knowledge/blob/master/fpga/fpga.md).

## GPU Design

Learn TensorRT and CUDA programing. Try examples on our TX2/TK1 platforms.

* [TensorRT](https://developer.nvidia.com/tensorrt)



# Research Related Topics

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


A more complete list is [here](https://github.com/doonny/basic_knowledge/blob/master/paper/fpga.md).


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
