## 如果你使用 Xilinx FPGA

### 首先咨询老师你的研究路线是下面哪条？

### 如果你的任务是基于FPGA进行算法加速
- 首先，学习王老师《异构计算》课程实验，配合阅读《Vitis Unified Software Platform Documentation, Application Acceleration Development》，学习掌握Vitis环境使用（仿真、硬件部署、对比硬件加速比）；
- 接下来，阅读《The HLS Book》和学习《Vitis High-Level Synthesis User Guide》，学习HLS代码优化方法；同时学习Xilinx官方Vitis Example代码（参考下面链接）；
- 最后，学习实验室PipeCNN-v2神经网络硬件加速器代码，学习分类、目标检测等实例代码。

### 如果你任务是基于zynq或者MPSOC处理器做设计
- 首先，学习Zynq处理器基本架构，详细阅读《The Zynq Book》，使用Zedboard，完成UG1165和《Zynq Book Tutorial》相关实验，学会PS启动和C/C++应用程序编写，学会使用Vivado/Vitis在PL端配置相关IP核（如GPIO、AXI-DMA、AXI-Stream接口等）；
- 接下来，学习高层次综合HLS方法设计IP核，阅读《The HLS Book》，学会在PL端设计算法加速电路；
- 最后，学习在Zynq处理器上启动Linxu、在Linux下设计应用程序，学习Petalinux使用，学习基于Vitis的算法硬件加速方法，参考UG1391，学习Github上Xilinx官方的2个教程[Vitis_Tutorial](https://github.com/Xilinx/Vitis-Tutorials)和Vitis_Accel_Examples（见下面链接）。


Best Book:
- [The Zynq Book](www.zynqbook.com) （新生入门必读）
- [Zynq MPSoC Book](https://www.zynq-mpsoc-book.com) 
- [Parallel Programming for FPGAs - The HLS Book](http://kastner.ucsd.edu/hlsbook/) （新生入门必读）

Board Tutorial:

- UG1165 Zynq-7000 SoC: Embedded Design Tutorial （新生入门必须完成的实验）
- UG1209 Zynq UltraScale+ MPSoC: Embedded Design Tutorial

Vitis:

- UG1393 Vitis Unified Software Platform Documentation, Application Acceleration Development  （必读）
- UG1400 Vitis Unified Software Platform Documentation, Embedded Software Development
- [官方Vitis入门教程含代码](https://github.com/Xilinx/Vitis-Tutorials) （新生入门必做: 01.Getting Started, 02.Hardware_Accelerators）
- [Vitis设计FPGA加速例程代码](https://github.com/Xilinx/Vitis_Accel_Examples) 和 [例程2](https://github.com/Xilinx/Vitis-HLS-Introductory-Examples)（入门后必读代码）
- UG1399 Vitis High-Level Synthesis User Guide （进阶必读）

Vivado:

- UG898 Vivado Design Suite User Guide, Embedded Processor Hardware Design
- UG893 Vivado Design Suite User Guide, Using the Vivado IDE

A few useful blogs:

- [Xilinx vitis学习教程：ZYNQ之Hello world](https://blog.csdn.net/longfei_3/article/details/103757018)

Xilinx Design Hub:

- [所有资料分门别类大汇总](https://www.xilinx.com/support/documentation-navigation/design-hubs.html)

## 如果你使用 Intel FPGA

* ''OpenCL Programming Guide'', Aaftab Munshi, et.al., 2012  [also known as The Green Book]
* [''FPGA异构计算——基于OpenCL的开发方法''](https://baike.baidu.com/item/FPGA%E5%BC%82%E6%9E%84%E8%AE%A1%E7%AE%97%E2%80%94%E2%80%94%E5%9F%BA%E4%BA%8EOpenCL%E7%9A%84%E5%BC%80%E5%8F%91%E6%96%B9%E6%B3%95), 黄乐天 等, 2015

Also, refers to Intel/Xilinx's OpenCL user guide to learn specific techniques that will be used in the project.

*  [''面向 OpenCL 的英特尔 FPGA SDK 最佳实践指南''](https://www.intel.cn/content/www/cn/zh/programmable/products/design-software/embedded-software-developers/opencl/support.html)

除此之外，需要学习官方文档:

- Intel FPGA SDK for OpenCL Pro Edition Programming Guide
- Intel FPGA SDK for OpenCL Pro Edition Best Practices Guide