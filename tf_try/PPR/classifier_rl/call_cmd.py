# coding: utf-8
"""
Call CMD to run train and test with 10 circulations at least.
"""

import subprocess

dataset = ['ksc', 'ip', 'pu', 'sa']

# train
for n in range(1):
    """
    for i in range(1):
        p = subprocess.Popen('python train.py '
                             + '--PPR_block cd --max_steps 20000 '
                             + '--dataset_name ' + dataset[i]
                             + ' --save_name ' + dataset[i] + '_0302_ppr8_' + str(n) + '/',
                             shell= True)
        print('--------------------dataset----------------------', dataset[i])
        p.wait()
"""

    for i in range(1):
        p = subprocess.Popen('python train.py '
                             + '--PPR_block cd '
                             + '--dataset_name ' + dataset[i]
                             + ' --neighbor 8 --conv1_stride 9 --max_steps 10000 '
                             + ' --save_name ' + dataset[i] + '_0308_ppr_' + str(n) + '_cube/',
                             shell= True)
        p.wait()
    """
# fine-tuning
for n in range(1, 2):

    for i in range(4):
        p = subprocess.Popen('python train.py '
                             + '--PPR_block cd '
                             + '--learning_rate 0.01 '
                             + '--ckpt_dir ' + dataset[i] + '_1107_' + str(n) + '/'
                             + ' --dataset_name ' + dataset[i]
                             + ' --save_name ' + dataset[i] + '_1118_' + str(n) + '/',
                             shell= True)
        print('--------------------dataset----------------------', dataset[i])
        p.wait()


    for i in range(4):
        p = subprocess.Popen('python train.py '
                             + '--PPR_block cd '
                             + '--learning_rate 0.01 '
                             + '--ckpt_dir ' + dataset[i] + '_1107_' + str(n) + '_cube/'
                             + ' --dataset_name ' + dataset[i]
                             + ' --neighbor 8 --conv1_stride 9'
                             + ' --save_name ' + dataset[i] + '_1118_' + str(n) + '_cube/',
                             shell= True)
        p.wait()

lr_mode = ['trangular', 'trangular2', 'exp']

for i in range(1):
    for j in range(3):
        p = subprocess.Popen('python train.py '
                             + '--PPR_block cd '
                             + '--dataset_name ' + dataset[i]
                             + ' --neighbor 8 --conv1_stride 9'
                             + ' --mode ' + lr_mode[j]
                             + ' --save_name ' + dataset[i] + '_0104_' + lr_mode[j] + '/',
                             shell=True)
        p.wait()"""