'''
This scrypt is used to calculate the possible values of VEC_SIZE and LANE_NUM
'''
import numpy as np

#AlexNet
layer_config = [[0,
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

# Configuration file instructions
[layer_type, # "0" -> conv, "1" -> fc

data_w, data_h, data_n, weight_w, weight_h, weight_n, weight_m, bias_size, #/memRd Parameters

memrd_src, #"0"-> data_buf  "1"-> output_buf  "2"->"fc_1_buffer"  "3"->"fc_2_buffer"  "4"->"pool_buffer" "5"->"eltwise_buf"(resnet)

conv_x, conv_y, conv_z, conv_stride, conv_padding, conv_split, conv_relu, #Conv Parameters

pool_on, pool_x, pool_y, pool_z, pool_size, pool_stride, # Pooling Parameters

lrn_on,# lrn on/off control

memwr_dst] = [i for i in range(25)]#"0"-> data_buf  "1"-> output_buf  "2"->"fc_1_buffer"  "3"->"fc_2_buffer"

#VEC_SIZE 需要大于等于4，并且除去输入层，其余各层都需要被weight_n整除, i.e., 4, 8, 16, ...；典型值为16
#LANE_NUM 需要大于1，对于alexnet: 2, 3, 4, 8, 12, 15, 16, 22, 28, 32, 34, 48, 50, 51, 64, ...; 典型值16
#
VEC_SIZE_LIST=[]
for vec_size in range(4,100):
    for ll in range(1,8):
        if (np.mod(layer_config[ll][weight_n],vec_size)!=0):
            break
    if(ll==7):
        VEC_SIZE_LIST.append(vec_size)
print(VEC_SIZE_LIST)

LANE_NUM_LIST=[]
for lan_num in range(2,100):
    for ll in range(1,8):
        if (np.mod(np.ceil(layer_config[ll][weight_m]/lan_num),2)!=0 and (layer_config[ll][conv_split]==1)):
            break
    if(ll==7):
        LANE_NUM_LIST.append(lan_num)
print(LANE_NUM_LIST)