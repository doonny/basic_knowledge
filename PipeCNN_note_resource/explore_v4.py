'''
Use different parameters to execute the PipeCNN.
功能： 自动修改VEC_SIZE，LANE_NUM参数，并且编译运行，将.aocx文件中包含的资源消耗信息和run.log文件中包含的每层运行时间信息收集到一个excel表格中。
注意事项：
    1. 首先修改makefile，选择hw，report，sw_emu，还要注意输出文件是aocx，还是aoco
    2. 要想运行run.exe，需要在当前工程目录下存放数据，但是每个工程目录都存一个data文件夹显然太大，所以需要在project文件夹下创建data的软链接
    3. 将本脚本放在和project同一级文件夹下
    4. 修改bashrc来选择板卡

CHANGES:
    1. 增加板卡的验证，去掉了修改环境变量的功能，比较鸡肋。在实际使用中请直接修改bashrc
    2. 增加是否删除Quartus工程的选项
    3. 将编译好的数据存入excel表格
    4. 使用subprocess替代部分system
    5. 去掉VEC_SIZE，LANE_NUM编译后参数检查功能（鸡肋），该在编译前使用calculate_parameters.py脚本计算得到。
    6. 增加读取.aocx和run_log.txt的功能，aocx涉及的硬件消耗信息和run_log.txt中的运行时间信息都会被采集到一个excel文件中！！！！
'''
import os
import subprocess
import json
import xlwt
import datetime

orig_dir = './project'
[HW,SW_EMU,REPORT] = [0,1,2]

########使用前需要注意修改此处配置#########
FUN_SEL = HW
LAYER_NUM = 8 #alex net 8层
CLEAN_PROJ = 1 #是否清理quartus工程；1：清理  0：不清理
#######################################

[de5_net, de10_std, de10_nano, de5a_net] = [ i for i in range(4) ]

def edit_make(proj_dir,VEC_SIZE, LANE_NUM, CONV_GP_SIZE_X):
    '''
    edit the 'hw_param.cl' file and run the 'make' command
    Args:
        proj_dir: the project dir that contains the "project" dir. e.g. /PipeCNN-master
        VEC_SIZE: the depth
        LANE_NUM:
        CONV_GP_SIZE_X:
    '''
    config_file = proj_dir + '/device/hw_param.cl'
    orig_config_file = config_file[0:-3]+'_orig.cl'

    if(os.path.exists(orig_config_file) == False):
        os.system('cp ' + config_file + ' ' + orig_config_file)

    out_data = ""
    with open(orig_config_file, 'r', encoding="utf-8") as f:
        for line in f:
            if '#define VEC_SIZE' in line:
                line = '#define VEC_SIZE            %d // larger than 4, i.e., 4, 8, 16, ...\n'%VEC_SIZE
            
            if '#define LANE_NUM' in line:
                line = '#define LANE_NUM            %d // larger than 1, for alexnet: 2, 3, 4, 8, 12, 15, 16, 22, 28, 32, 34, 48, 50, 51, 64, ...\n'%LANE_NUM
            
            if '#define CONV_GP_SIZE_X' in line:
                line = '#define CONV_GP_SIZE_X      %d\n'%CONV_GP_SIZE_X
            
            out_data += line

    with open(config_file, 'w', encoding='utf-8') as cfg_f:
        cfg_f.write(out_data)

    ##make clean
    os.system('make clean --directory' + ' ' + proj_dir)
    ##complie the RTL
    os.system('make --directory' + ' ' + proj_dir + '/device/RTL/')
    ##comple the Make
    os.system('make --directory' + ' ' + proj_dir + ' > ' + proj_dir + '/make_log.txt')

def run_emu(proj_dir):#run the emulation
    cmd1 = 'cd ' + proj_dir
    if FUN_SEL == SW_EMU:
        cmd2 = 'export CL_CONTEXT_EMULATOR_DEVICE_ALTERA=1'#use this cmd when doing the software emulation
    elif FUN_SEL == HW:
        cmd2 = 'echo'#use this cmd when using the fpga hardware
    cmd3 = './run.exe conv.aocx > run_log.txt'
    cmd4 = cmd1+'&&'+cmd2+'&&'+cmd3
    os.system(cmd4)

def clean_project(proj_dir, clean_sel):
    '''
    delet all the files in the "conv" folder, except the 'reports' dir in 'proj_dir/conv' dir.
    '''
    if clean_sel == 1:
        for item in os.listdir(proj_dir + '/conv'):
            item_path = os.path.join(proj_dir + '/conv',item)
            if(not(os.path.isdir(item_path)and('reports' in item))):
                os.system('rm -r ' + item_path)

def env_cfg(board):
    '''
    验证当前所选用板子在bashrc中是否配置正确
    '''
    if(board == de5_net):
        if ("de5net_a7" not in subprocess.getoutput("aoc -list-boards")):
            print("check the board config in ~/.bashrc")
            exit()
        board_cfg = "_de5_net"

    if(board == de10_std):##TODO
        if ("de5net_a7" not in subprocess.getoutput("aoc -list-boards")):
            print("check the board config in ~/.bashrc")
            exit()
        board_cfg = "_de10_std"   

    if(board == de10_nano):##TODO
        if ("de5net_a7" not in subprocess.getoutput("aoc -list-boards")):
            print("check the board config in ~/.bashrc")
            exit()
        board_cfg = "_de10_nano"

    if(board == de5a_net):
        if ("de5a_net_e1" not in subprocess.getoutput("aoc -list-boards")):
            print("check the board config in ~/.bashrc")
            exit()
        board_cfg = "_de5a_net"
    return board_cfg

def get_rpt_data(proj_dir):
    '''
    从report中读取信息
    '''
    report_dir = proj_dir + '/conv/reports/lib/json/summary.json'
    aa = json.load(open(report_dir))
    for item in aa['estimatedResources']['children']:
        if(item['name']=='Total'):
            break
    return item['data']+item['data_percent']

def decode_hw_log(ch,line):#
    '''
    将aocx文件中的资源消耗信息解码
    Args:
        ch:是b'ALUTs:'之类的“头”，要保留这些头后面的东西
    '''
    pt_end1 = line[len(ch):].find(b'\n')#找到结束位置
    pt_end2 = line[len(ch):].find(b' /')

    if pt_end1 < 0:
        pt_end1 = 100
    if pt_end2 < 0:
        pt_end2 = 100

    if pt_end1 < pt_end2:
        useful_data = line[len(ch):len(ch)+pt_end1]
    else:
        useful_data = line[len(ch):len(ch)+pt_end2]

    return float(useful_data.replace(b',',b''))#去掉','将并调整为整数

def get_hw_data(proj_dir):
    '''
    从aocx文件中获取信息
    '''
    fname = proj_dir + '/conv.aocx'
    hw_data = [0 for i in range(7)]
    res = [b'ALUTs:',b'Registers:',b'Logic utilization:',b'DSP blocks:',b'Memory bits:',b'RAM blocks:',b'Actual clock freq:']

    i = 0
    with open(fname,'rb') as aocxf:
        offset =-1500#从文件尾向前偏移的单位
        aocxf.seek(offset,2)
        lines=aocxf.readlines()
        for line in lines:
            for r in res:#查看line里是否包括res资源
                pt=line.find(r)
                if(pt!=-1):
                    hw_data[i]=decode_hw_log(r,line[pt:])
                    # print(line[pt+6:])
                    i += 1
            
        if i != len(res):
            print("get aocx information fail!!!!")
            exit()

    return hw_data

def get_run_data(proj_dir):
    fname = proj_dir + '/run_log.txt'
    run_data = [[0 for col in range(LAYER_NUM)] for row in range(5)]
    run_time = [b'MemRd: ', b'Conv : ', b'Pool : ', b'MemWr: ', b'Lrn  : ']
    with open(fname,'rb') as runf:
        offset =-1500#从文件尾向前偏移的单位
        runf.seek(offset,2)
        lines=runf.readlines()
        for i in range(len(lines)):#对每一层进行检查
            sp = lines[i].find(b'Layer-')#start point
            if(sp != -1):#如果是层数信息
                ep = lines[i].find(b':')#end point
                layer = int(lines[i][sp+len(b'Layer-'):ep])
                for j in range(len(run_time)):#对没一项时间进行检查
                    sp = lines[i+j+1].find(run_time[j])
                    if(sp != -1):
                        ep = lines[i+j+1].find(b' ms')
                        run_data[j][layer-1] = float(lines[i+j+1][sp+len(run_time[j]):ep])
                    else:
                        print('collect run time information fail!!!!')
                        exit()
    return run_data

def create_project(orig_dir, board_cfg, VEC_SIZE, LANE_NUM, CONV_GP_SIZE_X):
    '''
    本函数建立对应于不同VEC_SIZE,LANE_NUM,CONV_GP_SIZE_X参数的工程。
    不同的VEC_SIZE,LANE_NUM,CONV_GP_SIZE_X的工程都是有原始的“project”文件夹下的工程衍生而来。
    Argus：
        orig_dir:原始project文件夹
        board：不同的FPGA
    '''
    
    proj_dir = './project_vec%d_lan%d_gpx%d'%(VEC_SIZE, LANE_NUM, CONV_GP_SIZE_X) + board_cfg
    if os.path.exists(proj_dir):#若之前存在，则删除
        os.system('rm -rf ' + proj_dir)

    os.system('cp -r '+ orig_dir + ' ' + proj_dir)
    edit_make(proj_dir, VEC_SIZE, LANE_NUM, CONV_GP_SIZE_X)#修改参数并编译工程

    return proj_dir

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
if FUN_SEL == REPORT:
    # 创建一个worksheet
    report_sheet = workbook.add_sheet('Report')
    # 写入excel
    # 参数对应 行, 列, 值
    LAB_REPORT=['Board','VEC_SIZE','LANE_NUM','CONV_GP_SIZE_X','ALUTs','FFs','RAMs','DSPs','ALUTs%','FFs%','RAMs%','DSPs%']
    for i in range(len(LAB_REPORT)):
        report_sheet.write(0,i, label = LAB_REPORT[i])
if FUN_SEL == HW:
    report_sheet = workbook.add_sheet('Report')
    hwinfo_sheet = workbook.add_sheet('HW')
    runtim_sheet = workbook.add_sheet('Run time')

    LAB_REPORT=['Board','VEC_SIZE','LANE_NUM','CONV_GP_SIZE_X','ALUTs','FFs','RAMs','DSPs','ALUTs%','FFs%','RAMs%','DSPs%']
    for i in range(len(LAB_REPORT)):
        report_sheet.write(0,i, label = LAB_REPORT[i])

    LAB_HW=['Board','VEC_SIZE','LANE_NUM','CONV_GP_SIZE_X','ALUTs','Registers','Logic utilization','DSP blocks','Memory bits','RAM blocks','Actual clock freq']
    for i in range(len(LAB_HW)):
        hwinfo_sheet.write(0, i, label = LAB_HW[i])

    LAB_RUN=['Board','VEC_SIZE','LANE_NUM','CONV_GP_SIZE_X', 'Function']+[('Layer-%d'%(i+1)) for i in range(LAYER_NUM)]
    for i in range(len(LAB_RUN)):
        runtim_sheet.write(0, i, label = LAB_RUN[i])

row = 1
for VEC_SIZE in [16]:     #larger than 4, i.e., 4, 8, 16
    for LANE_NUM in [8, 22]:     #larger than 1, for alexnet: 2, 3, 4, 8, 12, 15, 16, 22, 28, 32, 34, 48, 50, 51, 64, ...
        for CONV_GP_SIZE_X in [7]:
            for board in [de5_net]:#[de5_net, de10_std, de10_nano, de5a_net]
                board_cfg = env_cfg(board)#验证bashrc所配置的环境
                proj_dir = create_project(orig_dir, board_cfg, VEC_SIZE, LANE_NUM, CONV_GP_SIZE_X)#建立并编译工程

                if FUN_SEL == REPORT:
                    #获取report信息并存储
                    rpt_data = get_rpt_data(proj_dir)
                    report_sheet.write(row, 0, label=board_cfg[1:])
                    report_sheet.write(row, 1, label=VEC_SIZE)
                    report_sheet.write(row, 2, label=LANE_NUM)
                    report_sheet.write(row, 3, label=CONV_GP_SIZE_X)
                    for col in range(len(rpt_data)):
                        report_sheet.write(row, 4+col, label=rpt_data[col])

                    row = row + 1

                if FUN_SEL == HW:
                    run_emu(proj_dir)#run.exe conv.aocx
                    #获取report信息并存储
                    rpt_data = get_rpt_data(proj_dir)
                    report_sheet.write(row,0,label=board_cfg[1:])
                    report_sheet.write(row,1,label=VEC_SIZE)
                    report_sheet.write(row,2,label=LANE_NUM)
                    report_sheet.write(row,3,label=CONV_GP_SIZE_X)
                    for col in range(len(rpt_data)):
                        report_sheet.write(row,4+col,label=rpt_data[col])
                    
                    #获取aocx中的信息并存储
                    hw_data = get_hw_data(proj_dir)
                    hwinfo_sheet.write(row,0,label=board_cfg[1:])
                    hwinfo_sheet.write(row,1,label=VEC_SIZE)
                    hwinfo_sheet.write(row,2,label=LANE_NUM)
                    hwinfo_sheet.write(row,3,label=CONV_GP_SIZE_X)
                    for col in range(len(hw_data)):
                        hwinfo_sheet.write(row,4+col,label=hw_data[col])
                    
                    #获取run_log.txt中的时间消耗信息
                    run_data = get_run_data(proj_dir)

                    runtim_sheet.write((row-1)*6+1,0,label=board_cfg[1:])
                    runtim_sheet.write((row-1)*6+1,1,label=VEC_SIZE)
                    runtim_sheet.write((row-1)*6+1,2,label=LANE_NUM)
                    runtim_sheet.write((row-1)*6+1,3,label=CONV_GP_SIZE_X)

                    LAB_FUN = ['MemRd', 'Conv', 'Pool', 'MemWr', 'Lrn']
                    for fun in range(5):
                        runtim_sheet.write((row-1)*6+fun+1,4,label=LAB_FUN[fun])
                        for col in range(LAYER_NUM):
                            runtim_sheet.write((row-1)*6+fun+1,col+5,label=run_data[fun][col])

                    row = row + 1

                elif FUN_SEL == SW_EMU:
                    run_emu(proj_dir)#run.exe conv.aocx
                    run_data = get_run_data(proj_dir)

                    runtim_sheet.write((row-1)*6+1,0,label=board_cfg[1:])
                    runtim_sheet.write((row-1)*6+1,1,label=VEC_SIZE)
                    runtim_sheet.write((row-1)*6+1,2,label=LANE_NUM)
                    runtim_sheet.write((row-1)*6+1,3,label=CONV_GP_SIZE_X)

                    LAB_FUN = ['MemRd', 'Conv', 'Pool', 'MemWr', 'Lrn']
                    for fun in range(5):#对于每一层包含的每个功能
                        runtim_sheet.write((row-1)*6+fun+1,4,label=LAB_FUN[fun])
                        for col in range(LAYER_NUM):
                            runtim_sheet.write((row-1)*6+fun+1,col+5,label=run_data[fun][col])
                            
                    row = row + 1
                
                clean_project(proj_dir, CLEAN_PROJ)#选择是否清除Quartus工程，默认0不清除
    
if FUN_SEL == REPORT or FUN_SEL == HW:
    workbook.save('report_%s.xls'%datetime.datetime.now().strftime('%Y_%m_%d_%H_%M'))