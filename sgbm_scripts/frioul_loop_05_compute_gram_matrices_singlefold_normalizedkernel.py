# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:45:11 2012

@author: auzias
"""


#import commands
import subprocess
import os
import os.path as op
import numpy as np

coderoot_dir = '/netapp/vol1_psy/basepsy/FS60/SGBM_Github/sgbm/sgbm_scripts'



n_sl_points_list = [2500]
graph_type = 'radius'
n_folds = 10
#graph_params_list = np.arange(90,28,-5)
graph_params_list = [50]

hemispheres_list = ['lh', 'rh']
experiment = 'searchlight_HC_SZ_radius_50'
for graph_param in graph_params_list:
    for hem in hemispheres_list:
        for n_sl_points in n_sl_points_list:
            for fold_ind in range(n_folds):
                #cmd = "frioul_batch -w 168 'python %s/05_compute_gram_matrices_singlefold_normalizedkernel.py %s %s %s %d %d %d'" % (coderoot_dir, experiment, hem, graph_type, graph_param, n_sl_points, fold_ind)
                #cmd = "qsub -cwd -q all.q -b y -V python %s/05_compute_gram_matrices_singlefold_normalizedkernel.py %s %s %s %d %d %d" % (coderoot_dir, experiment, hem, graph_type, graph_param, n_sl_points, fold_ind)
                cmd = "qsub -cwd -q all.q -b y -V -e /netapp/vol1_psy/basepsy/FS60/%s/log_files/loop05_%s_%d_%d_%d_errors.txt -o /netapp/vol1_psy/basepsy/FS60/%s/log_files/loop05_%s_%d_%d_%d_output.txt python %s/05_compute_gram_matrices_singlefold_normalizedkernel.py %s %s %s %d %d %d" % (experiment, hem, graph_param, n_sl_points, fold_ind, experiment, hem, graph_param, n_sl_points, fold_ind, coderoot_dir, experiment, hem, graph_type, graph_param, n_sl_points, fold_ind)
                #a = commands.getoutput(cmd)
                a = subprocess.call(cmd, shell=True)
                print(cmd)
