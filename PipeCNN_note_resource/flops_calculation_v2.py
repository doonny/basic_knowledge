# 本程序用来计算给定网络的计算量

import numpy as np
import xlwt
import matplotlib.pyplot as plt

DDR_BANDWIDTH = 95400000000*2 #bits/s
DATA_WIDTH = 8 #数据宽度为8bits

#AlexNet
LAYER_NUM = 8
NUM_CONFIG_ITEM = 25
layer_config_original = [[0,
                227, 227, 3, 11, 11, 3, 96, 96,
                0,
                55, 55, 96, 4, 0, 0, 1,
                1, 27, 27, 96, 3, 2,
                1,
                1],#Layer-1
                [0,
                27, 27, 96, 5, 5, 48, 256, 256,
                0,
                27, 27, 256, 1, 2, 1, 1,
                1, 13, 13, 256, 3, 2,
                1,
                1],#Layer-2
                [0,
                13, 13, 256, 3, 3, 256, 384, 384,
                0,
                13, 13, 384, 1, 1, 0, 1,
                0, 13, 13, 384, 0, 0,
                0,
                1],#Layer-3
                [0,
                13, 13, 384, 3, 3, 192, 384, 384,
                1,
                13, 13, 384, 1, 1, 1, 1,
                0, 13, 13, 384, 0, 0,
                0,
                0],#Layer-4
                [0,
                13, 13, 384, 3, 3, 192, 256, 256,
                0,
                13, 13, 256, 1, 1, 1, 1,
                1, 6, 6, 256, 3, 2,
                0,
                1],#Layer-5  Note: for last conv layer, outputs are write to fc buffer
                [1,
                6, 6, 256, 6, 6, 256, 4096, 4096,  # Note: The input size (dim1/dim2) is the combined data size (batched)
                4,
                1, 1, 4096, 6, 0, 0, 1,
                0, 1, 1, 4096, 0, 0,
                0,
                2],#Layer-6 fc
                [1,
                1, 1, 4096, 1, 1, 4096, 4096, 4096,
                2,
                1, 1, 4096, 1, 0, 0, 1,
                0, 1, 1, 4096, 0, 0,
                0,
                3],#Layer-7 fc
                [1,
                1, 1, 4096, 1, 1, 4096, 1024, 1024,
                3,
                1, 1, 1024, 1, 0, 0, 0,
                0, 1, 1, 1024, 0, 0,
                0,
                2]]#Layer-8 fc

# ##VGG
# LAYER_NUM = 16
# NUM_CONFIG_ITEM = 25
# layer_config_original = [[0,
#                 224, 224, 3, 3, 3, 3, 64, 64,
#                 0,
#                 224, 224, 64, 1, 1, 0, 1,
#                 0, 224, 224, 64, 0, 0,
#                 0,
#                 1],#Layer-1 (conv1_1)
#                 [0,
#                 224, 224, 64, 3, 3, 64, 64, 64,
#                 1,
#                 224, 224, 64, 1, 1, 0, 1,
#                 1, 112, 112, 64, 2, 2,
#                 0,
#                 0],#Layer-2 (conv1_2)
#                 [0,
#                 112, 112, 64, 3, 3, 64, 128, 128,
#                 4,
#                 112, 112, 128, 1, 1, 0, 1,
#                 0, 112, 112, 128, 0, 0,
#                 0,
#                 1],#Layer-3 (conv2_1)
#                 [0,
#                 112, 112, 128, 3, 3, 128, 128, 128,
#                 1,
#                 112, 112, 128, 1, 1, 0, 1,
#                 1, 56, 56, 128, 2, 2,
#                 0,
#                 0],#Layer-4 (conv2_2)
#                 [0,
#                 56, 56, 128, 3, 3, 128, 256, 256,
#                 4,
#                 56, 56, 256, 1, 1, 0, 1,
#                 0, 56, 56, 256, 0, 0,
#                 0,
#                 1],#Layer-5 (conv3_1)
#                 [0,
#                 56, 56, 256, 3, 3, 256, 256, 256,
#                 1,
#                 56, 56, 256, 1, 1, 0, 1,
#                 0, 56, 56, 256, 0, 0,
#                 0,
#                 0],#Layer-6 (conv3_2)
#                 [0,
#                 56, 56, 256, 3, 3, 256, 256, 256,
#                 0,
#                 56, 56, 256, 1, 1, 0, 1,
#                 1, 28, 28, 256, 2, 2,
#                 0,
#                 1],#Layer-7 (conv3_3)
#                 [0,
#                 28, 28, 256, 3, 3, 256, 512, 512,
#                 4,
#                 28, 28, 512, 1, 1, 0, 1,
#                 0, 28, 28, 512, 0, 0,
#                 0,
#                 0],#Layer-8  (conv4_1)
#                 [0,
#                 28, 28, 512, 3, 3, 512, 512, 512,
#                 0,
#                 28, 28, 512, 1, 1, 0, 1,
#                 0, 28, 28, 512, 0, 0,
#                 0,
#                 1],#Layer-9  (conv4_2)
#                 [0,
#                 28, 28, 512, 3, 3, 512, 512, 512,
#                 1,
#                 28, 28, 512, 1, 1, 0, 1,
#                 1, 14, 14, 512, 2, 2,
#                 0,
#                 0],#Layer-10 (conv4_3)
#                 [0,
#                 14, 14, 512, 3, 3, 512, 512, 512,
#                 4,
#                 14, 14, 512, 1, 1, 0, 1,
#                 0, 14, 14, 512, 0, 0,
#                 0,
#                 1],#Layer-11  (conv5_1)
#                 [0,
#                 14, 14, 512, 3, 3, 512, 512, 512,
#                 1,
#                 14, 14, 512, 1, 1, 0, 1,
#                 0, 14, 14, 512, 0, 0,
#                 0,
#                 0],#Layer-12  (conv5_2)
#                 [0,
#                 14, 14, 512, 3, 3, 512, 512, 512,
#                 0,
#                 14, 14, 512, 1, 1, 0, 1,
#                 1, 7, 7, 512, 2, 2,
#                 0,
#                 1],#Layer-13  (conv5_3)    Note: for last conv layer, outputs are write to fc buffer
#                 [1,
#                 7, 7, 512, 7, 7, 512, 4096, 4096,
#                 4,
#                 1, 1, 4096, 7, 0, 0, 1,
#                 0, 1, 1, 4096, 0, 0,
#                 0,
#                 2],#Layer-14  (fc6)
#                 [1,
#                 1, 1, 4096, 1, 1, 4096, 4096, 4096,
#                 2,
#                 1, 1, 4096, 1, 0, 0, 1,
#                 0, 1, 1, 4096, 0, 0,
#                 0,
#                 3],#Layer-15  (fc7)
#                 [1,
#                 1, 1, 4096, 1, 1, 4096, 1024, 1024,
#                 3,
#                 1, 1, 1024, 1, 0, 0, 0,
#                 0, 1, 1, 1024, 0, 0,
#                 0,
#                 2]#Layer-16  (fc8)
#                 ]

# Configuration file instructions
[layer_type, # "0" -> conv, "1" -> fc

data_w, data_h, data_n, weight_w, weight_h, weight_n, weight_m, bias_size, #/memRd Parameters

memrd_src, #"0"-> data_buf  "1"-> output_buf  "2"->"fc_1_buffer"  "3"->"fc_2_buffer"  "4"->"pool_buffer" "5"->"eltwise_buf"(resnet)

conv_x, conv_y, conv_z, conv_stride, conv_padding, conv_split, conv_relu, #Conv Parameters

pool_on, pool_x, pool_y, pool_z, pool_size, pool_stride, # Pooling Parameters

lrn_on,# lrn on/off control

memwr_dst] = [i for i in range(25)]#"0"-> data_buf  "1"-> output_buf  "2"->"fc_1_buffer"  "3"->"fc_2_buffer"

[CONV_LAYER, FC_LAYER] = [0, 1]#与上面的layer_type想对应

def vail_vec_lan(layer_config):
    '''
    计算VEC_SIZE 和 LANE_NUM的可能值
    VEC_SIZE 需要大于等于4，并且除去输入层，其余各层都需要被weight_n整除, i.e., 4, 8, 16, ...；典型值为16
    LANE_NUM 需要大于1，对于alexnet: 2, 3, 4, 8, 12, 15, 16, 22, 28, 32, 34, 48, 50, 51, 64, ...; 典型值16
    '''
    vec_size_list=[]
    for vec_size in range(4,100):
        for ll in range(1,LAYER_NUM):
            if (np.mod(layer_config[ll][weight_n],vec_size)!=0):
                break
        if(ll==LAYER_NUM-1):
            vec_size_list.append(vec_size)

    lane_num_list=[]
    for lan_num in range(2,100):
        for ll in range(1,LAYER_NUM):
            if (np.mod(np.ceil(layer_config[ll][weight_m]/lan_num),2)!=0 and (layer_config[ll][conv_split]==1)):
                break
        if(ll==LAYER_NUM-1):
            lane_num_list.append(lan_num)
    
    return vec_size_list,lane_num_list#返回可能的vec_size和lane_num


def cal_ftp(layer_config, layer_config_original, layer_num, vec_size, lane_num, frequency):
    '''
    计算神经网络中每层的"计算量flops","吞吐量turoughput"和"参数量paras"
    Input Args:
    layer_config: 网络的配置参数
    layer_config_original：在prepare()操作之前的原始网络参数
    layer_num：总共网络的层数
    vec_size，lane_num：并行度参数
    frequency：FPGA运行频率，可以在conv.aocx文件中找到

    Output Args:
    flops：返回每层的计算量
    time_layer：每层网络消耗的时间
    paras：每层网络的参数量
    conv_time_group：每组的卷积时间
    read_time_group：每组读取数据的时间
    '''
    flops = [ 0 for i in range(layer_num)]#每层的计算量
    time_layer = [ 0 for i in range(layer_num)]#每层的消耗时间
    paras = [ 0 for i in range(layer_num)]#每层的参数量

    conv_time_group = [ 0 for i in range(layer_num)]#每层网络，每组卷积时间
    read_time_group = [ 0 for i in range(layer_num)]#每层网络，每组读取时间
    
    for ll in range(layer_num):
        #这里mac记为两个运算，即“加法”和“乘法”，所以计算量是×2的，并且加上了bias的加法运算
        flops[ll] = 2 * layer_config[ll][weight_w] * layer_config[ll][weight_h] * layer_config[ll][weight_n] * layer_config[ll][conv_x] * layer_config[ll][conv_y] * layer_config[ll][weight_m]
        
        if(layer_config[ll][layer_type]==CONV_LAYER):#卷积层的瓶颈在于卷积计算
            time_layer[ll] = flops[ll]/(2*vec_size*lane_num*frequency)
            X = 7#一个组里面有几个卷积
        elif(layer_config[ll][layer_type]==FC_LAYER):#全连接层的瓶颈在于读取数据，数据的尺寸和卷积核尺寸相等，并且读入的是补零前的原始数据
            time_layer[ll] = layer_config_original[ll][weight_w] * layer_config_original[ll][weight_h] * layer_config_original[ll][weight_n] * layer_config_original[ll][weight_m] * DATA_WIDTH / DDR_BANDWIDTH #加载weight
            time_layer[ll] += layer_config_original[ll][weight_w] * layer_config_original[ll][weight_h] * layer_config_original[ll][weight_n] * DATA_WIDTH / DDR_BANDWIDTH #加载数据
            X = 1
        paras[ll] = layer_config[ll][weight_w] * layer_config[ll][weight_h] * layer_config[ll][weight_n] * layer_config[ll][weight_m]#每层参数个数

        conv_time_group[ll] = layer_config[ll][weight_w]*layer_config[ll][weight_h]*layer_config[ll][weight_n] * X * lane_num/(lane_num*vec_size*frequency)
        read_time_group[ll] = (((X - 1) * layer_config_original[ll][conv_stride] + layer_config_original[ll][weight_w]) * layer_config_original[ll][weight_h]*layer_config_original[ll][weight_n]+layer_config_original[ll][weight_w]*layer_config_original[ll][weight_h]*layer_config_original[ll][weight_n]*lane_num) * DATA_WIDTH / DDR_BANDWIDTH

    return flops, time_layer, paras, conv_time_group, read_time_group

def prepare(layer_config_original, layer_num, vec_size, lane_num):
    '''
    类似于host端的prepare()函数
    '''
    layer_config = [[0 for i in range(NUM_CONFIG_ITEM)] for j in range(layer_num)]
    for ll in range(layer_num):

        #First, create a new layer config
        for ii in range(NUM_CONFIG_ITEM):
            layer_config[ll][ii] = layer_config_original[ll][ii]
        
        #Second, perform padding on dim4, when it is not divisible by LANE_NUM
        if(layer_config[ll][weight_m]%lane_num != 0):
            layer_config[ll][weight_m] = np.ceil(float(layer_config[ll][weight_m])/lane_num)*lane_num
            layer_config[ll][bias_size] = layer_config[ll][weight_m]
    #对输入图像的深度进行扩展，使其是VEC_SIZE的公倍数
    layer_config[0][weight_n] = np.ceil(float(layer_config[0][weight_n])/vec_size)*vec_size
    layer_config[0][data_n] = layer_config[0][weight_n]
    return layer_config

## 主功能
flops_orig, time_layer_orig, paras_orig, a, b = cal_ftp(layer_config_original,layer_config_original, LAYER_NUM, 1, 1,1)#原始网络每层的时间消耗没有太大意义

vec_size_list = [4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,16,16,16,16,16]
lane_num_list = [2,4,8,16,22,32,64,2,4,8,16,22,28,32,48,2,4,8,16,22]
frequency_list= [249.3,249.4,240.6,238.1,222.3,216.5,204.2,254.1,252.9,241.1,225.6,188,195.5,198.9,155.9,264.7,248.9,232.3,229.1,78.76]#频率

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet1 = workbook.add_sheet('total time')

if not(len(vec_size_list)==len(lane_num_list) and len(lane_num_list)==len(frequency_list)):
    print("Check the vec_size list and lane_num_list and frequency_list!!")
    exit()
# 创建表格表头
for i in range(3 + LAYER_NUM):
    if i == 0:
        worksheet1.write(i,0,label='VEC_SIZE')
    if i == 1:
        worksheet1.write(i,0,label='LANE_NUMBER')
    if i == 2:
        worksheet1.write(i,0,label='Totle time')
    if i >= 3:
        worksheet1.write(i,0,label='Layer-%d'%(i-2))
# 分别将网络的总耗时和每层的耗时写入表格
for i in range(len(vec_size_list)):
    layer_config = prepare(layer_config_original, LAYER_NUM, vec_size_list[i], lane_num_list[i])
    flops, time_layer, paras, a, b= cal_ftp(layer_config, layer_config_original, LAYER_NUM, vec_size_list[i],lane_num_list[i], (frequency_list[i]*1000000))
    worksheet1.write(0,1+i,label=vec_size_list[i])
    worksheet1.write(1,1+i,label=lane_num_list[i])
    worksheet1.write(2,1+i,label=(1000*np.sum(time_layer)))
    
    for j in range(LAYER_NUM):
        worksheet1.write(3+j,1+i,label='%.2f'%(1000*time_layer[j]))

workbook.save('flops.xls')

# 每层卷积和读取数据时间对比
LAYER = -3#对选定的VEC_SIZE LANE_NUM进行观察每个group的时间
layer_config = prepare(layer_config_original, LAYER_NUM, vec_size_list[LAYER], lane_num_list[LAYER])
flops, time_layer, paras, a, b= cal_ftp(layer_config, layer_config_original, LAYER_NUM, vec_size_list[LAYER],lane_num_list[LAYER], (frequency_list[LAYER]*1000000))

plt.figure()
plt.bar(np.arange(LAYER_NUM)+1, b, alpha=0.5, width=0.3, color='yellow', edgecolor='red', label='read time', lw=3)
plt.bar(np.arange(LAYER_NUM)+1+0.4, a, alpha=0.2, width=0.3, color='green', edgecolor='blue', label='conv time', lw=3)
plt.legend(loc='upper left')
plt.title("time consumption for reading and conving")
plt.show()