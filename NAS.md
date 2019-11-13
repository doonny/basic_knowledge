# NAS paper list

## 综述

NAS 的基本思路是给定一个称为搜索空间的候选神经网络结构集合，用某种策略从中搜索出最优网络结构。神经网络结构的优劣即性能用某些指标如精度、速度来度量，称为性能评估。**搜索空间，搜索策略和性能评估策略**是NAS问题的三个核心要素。
![20191111155645.png](http://image.jingsnow.com/image/20191111155645.png)


|  Title  | Venue    | Search Method   | Memory Consumption(supernet)     |  Code |
|:--------|:--------:|:--------:|:--------:|:--------:|
| [Neural Architecture Search with reinforcement learning](https://arxiv.org/abs/1611.01578) | ICLR 2017  | RL-based | -  | - |
| [Learning Transferable Architectures for Scalable Image Recognition](https://arxiv.org/abs/1707.07012) | CVPR 2018  | RL-based | -  | - |
| [Progressive Neural Architecture Search](https://arxiv.org/abs/1712.00559) | ECCV 2018  | RL-based | -  | - |
| [MnasNet: Platform-Aware Neural Architecture Search for Mobile](https://arxiv.org/abs/1807.11626?context=cs.LG) | CVPR 2019  | RL-based | -  | - |
| [Regularized Evolution for Image Classifier Architecture Search](https://arxiv.org/abs/1802.01548) | AAAI 2019  | EA-based | -  | - |
| [DARTS: Differentiable Architecture Search](https://arxiv.org/abs/1806.09055) | ICLR 2019  | Grident-based | whole supernet |[github](https://github.com/quark0/darts)|
| [ProxylessNAS: Direct Neural Architecture Search on Target Task and Hardware](https://arxiv.org/pdf/1812.00332.pdf) | ICLR 2019  | RL+GD | Two paths  |[github](https://github.com/MIT-HAN-LAB/ProxylessNAS)|
| [Progressive Differentiable Architecture Search: Bridging the Depth Gap between Search and Evaluation](https://arxiv.org/abs/1904.12760) | 2019.04 arxiv  | Grident-based | whole supernet  |[github](https://github.com/chenxin061/pdarts)|
| [PC-DARTS: Partial Channel Connections for Memory-Efficient Differentiable Architecture Search](https://arxiv.org/abs/1907.05737v1) | 2019.07 arxiv  | Grident-based | whole supernet  |[github](https://github.com/yuhuixu1993/PC-DARTS)|
| [Densely Connected Search Space for More Flexible Neural Architecture Search](https://arxiv.org/abs/1906.09607) | 2019.06 arxiv  | Grident-based | whole supernet  |[github](https://github.com/JaminFong/DenseNAS)|
| [Efficient Neural Architecture Search via Parameter Sharing](https://arxiv.org/abs/1802.03268) | ICML 2018  | RL-based | Single path  |[github](https://github.com/carpedm20/ENAS-pytorch)|
| [Single-Path NAS: Designing Hardware-Efficient ConvNets in less than 4 Hours](https://arxiv.org/abs/1904.02877?context=cs) | 2019.04 arxiv  | RL-based | Single path with super kernels  |[github](https://github.com/dstamoulis/single-path-nas)|
| [Single Path One-Shot Neural Architecture Search with Uniform Sampling](https://arxiv.org/abs/1904.00420?context=cs.CV) | 2019.03.31 arxiv  | EA-based | Single path |[github](https://github.com/megvii-model/SinglePathOneShot)|
| [FairNAS: Rethinking Evaluation Fairness of Weight Sharing Neural Architecture Search](https://arxiv.org/abs/1907.01845) | 2019.07.03 arxiv  | RL+EA | Single path |[github](https://github.com/xiaomi-automl/FairNAS)|


