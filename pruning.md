# Pruning Read List

## Non-Structured Pruning

|  Title  | Venue    | Method   | Type     |  Code |
|:--------|:--------:|:--------:|:--------:|:--------:|
| [Learning both Weights and Connections for Efficient Neural Networks](https://arxiv.org/abs/1506.02626) | NIPS 2015 | Absolute value metric | Weights-Pruning  |[github](https://github.com/jack-willturner/DeepCompression-PyTorch)|
|[Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding](https://arxiv.org/abs/1510.00149)| ICLR 2016 (best paper)| Deep Compression| Weights-Pruning | [github](https://github.com/jack-willturner/DeepCompression-PyTorch)| | 
|[Dynamic Network Surgery for Efficient DNNs](https://arxiv.org/abs/1608.04493)| NIPS 2016 | Dynamic Pruning | Weights-Pruning | [github](https://github.com/yiwenguo/Dynamic-Network-Surgery)|
|[Bayesian Compression for Deep Learning](https://papers.nips.cc/paper/6921-bayesian-compression-for-deep-learning.pdf) | NIPS 2017 | Bayesian | Weights-Pruning | [github](https://github.com/KarenUllrich/Tutorial_BayesianCompressionForDL)|
|[A Systematic DNN Weight Pruning Framework using Alternating Direction Method of Multipliers](https://arxiv.org/abs/1804.03294)| ECCV 2018 | ADMM | Weights-Pruning | [github](https://github.com/KaiqiZhang/admm-pruning)|
| [To prune, or not to prune: exploring the efficacy of pruning for model compression](https://arxiv.org/abs/1710.01878)| ICLR 2018 | Progressive Pruning | Weights-Pruning | - |  
| [Frequency-Domain Dynamic Pruning for Convolutional Neural Networks](https://papers.nips.cc/paper/7382-frequency-domain-dynamic-pruning-for-convolutional-neural-networks.pdf)| NIPS 2018 | DCT Frequency-Domain Pruning | Weights-Pruning | - | 
[CLIP-Q: Deep Network Compression Learning by In-Parallel Pruning-Quantization](http://www.sfu.ca/~ftung/papers/clipq_cvpr18.pdf)| CVPR 2018 | Pruning & mix-Quantization | Weights | - | 
| [ADMM-NN: An Algorithm-Hardware Co-Design Framework of DNNs Using Alternating Direction Methods of Multipliers](https://dl.acm.org/citation.cfm?id=3304076)| ASPLOS 2019 | ADMM Pruning&Quantization Hardware Co-Design | Weights-Pruning | - |
| [SNIP: Single-shot Network Pruning based on Connection Sensitivity](https://arxiv.org/abs/1810.02340) | ICLR 2019 | One-shot Pruning | Weights-Pruning | [github](https://github.com/namhoonlee/snip-public)|
| [Energy-Constrained Compression for Deep Neural Networks via Weighted Sparse Projection and Layer Input Masking](https://openreview.net/forum?id=BylBr3C9K7)  |  ICLR 2019 | Energy-Constrained Pruning | Weights-Pruning | [github](https://github.com/hyang1990/model_based_energy_constrained_compression)|
| [The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://openreview.net/forum?id=rJl-b3RcF7) | ICLR 2019 (best paper)| Lottery Ticket Hypothesis | Weights-Pruning | [github](https://github.com/rahulvigneswaran/Lottery-Ticket-Hypothesis-in-Pytorch) | 



## Structured Pruning

|  Title  | Venue    | Method   | Type     |  Code |
|:--------|:--------:|:--------:|:--------:|:--------:|
|[Learning Structured Sparsity in Deep Neural Networks](https://papers.nips.cc/paper/6504-learning-structured-sparsity-in-deep-neural-networks.pdf)| NIPS 2016   | Group Lasso | Filter-Pruning | - |
|[Channel Pruning for Accelerating Very Deep Neural Networks](https://arxiv.org/pdf/1707.06168v2.pdf) | ICCV 2017 | Lasso | Filter-Pruning | [github](https://github.com/yihui-he/channel-pruning) |
| [Pruning Filters for Efficient ConvNets]((https://arxiv.org/abs/1608.08710))| ICLR 2017 | L1 norm metric | Filter-Pruning | [github](https://github.com/rahulvigneswaran/Lottery-Ticket-Hypothesis-in-Pytorch) | - |
| [ThiNet: A Filter Level Pruning Method for Deep Neural Network Compression](https://arxiv.org/abs/1707.06342)| ICCV 2017  | L1 norm metric | Filter-Pruning|[github](https://github.com/Roll920/ThiNet)|
| [Pruning Convolutional Neural Networks for Resource Efficient Inference](https://arxiv.org/abs/1611.06440)| ICLR 2017 | Taylor expansion | Filter-Pruning | [github](https://github.com/Tencent/PocketFlow#channel-pruning)|
| [AMC: Automl for model compression and acceleration on mobile devices](https://arxiv.org/abs/1802.03494) | ECCV 2018 | AutoML | Filter-Pruning | [github](https://github.com/mit-han-lab/amc-release)|
|[Soft Filter Pruning for Accelerating Deep Convolutional Neural Networks]()| IJCAI 2018 | Soft Filter Pruning | Filter-Pruning |[github](https://github.com/he-y/soft-filter-pruning)|
|[Accelerating Convolutional Networks via Global & Dynamic Filter Pruning](https://www.ijcai.org/proceedings/2018/0336.pdf) | IJCAI 2018 | Global Filter Pruning | Filter-Pruning | - |
| [ADAM-ADMM: A Unified, Systematic Framework of Structured Weight Pruning for DNNs](https://www.semanticscholar.org/paper/ADAM-ADMM%3A-A-Unified%2C-Systematic-Framework-of-for-Zhang-Zhang/64db2e2c76aa3f028b6866f91795a7c005a3f13b) | NIPS 2018 | ADMM | Filter-Pruning | [github](https://github.com/KaiqiZhang/ADAM-ADMM)|
|[MetaPruning: Meta Learning for Automatic Neural Network Channel Pruning](https://arxiv.org/abs/1903.10258) | 	ICCV 2019 | Meta Learning & Genetic algorithm | Filter-Pruning | [github](https://github.com/liuzechun/MetaPruning)|