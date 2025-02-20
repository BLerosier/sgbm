# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:45:11 2012

@author: takerkart
"""


#import commands
import subprocess
import os
import os.path as op
import numpy as np

coderoot_dir = '/netapp/vol1_psy/basepsy/FS60/SGBM_Github/sgbm/sgbm_scripts'



n_sl_points_list = [2500]
hemispheres_list = ['lh','rh']
graph_type = 'radius'
#graph_params_list = np.arange(30,92,5)
graph_params_list = [50]
n_permuts = 5000
experiment = 'searchlight_HC_SZ_radius_50'

for graph_param in graph_params_list:
    for hem in hemispheres_list:
        for n_sl_points in n_sl_points_list:
            #cmd = "frioul_batch 'python %s/07_permuted_searchlight_classif.py %s %s %s %d %d %d'" % (coderoot_dir, experiment, hem, graph_type, graph_param, n_sl_points, n_permuts)
            #cmd = "qsub -cwd -q all.q -b y -V python %s/07_permuted_searchlight_classif.py %s %s %s %d %d %d" % (coderoot_dir, experiment, hem, graph_type, graph_param, n_sl_points, n_permuts)
            cmd = "qsub -cwd -q all.q -b y -V -e /netapp/vol1_psy/basepsy/FS60/%s/log_files/loop07_%s_%d_%d_%d_errors.txt -o /netapp/vol1_psy/basepsy/FS60/%s/log_files/loop07_%s_%d_%d_%d_output.txt python %s/07_permuted_searchlight_classif.py %s %s %s %d %d %d" % (experiment, hem, graph_param, n_sl_points, n_permuts, experiment, hem, graph_param, n_sl_points, n_permuts, coderoot_dir, experiment, hem, graph_type, graph_param, n_sl_points, n_permuts)
            #a = commands.getoutput(cmd)
            a = subprocess.call(cmd, shell=True)
            print(cmd)
