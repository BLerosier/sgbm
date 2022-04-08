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
#n_permuts = 5000
n_permuts = 5000
#graph_param_list = np.arange(30,92,5)
graph_param_list = [50]
n_scales_list = np.arange(1,len(graph_param_list)+1,2)
# threshold used on the point statistics to define clusters; since the statistics we use is a z-score, we use a 1.645 threshold (eq to p<0.05)
#threshold_list = [1.282, 1.645, 2.326, 2.576, 2.878, 3.090, 3.290, 3.719]
#one_sided_p_values = [0.1, 0.05, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0001]
threshold_list = [1.645, 2.326, 2.576, 3.090]
one_sided_p_values = [0.05, 0.01, 0.005, 0.001]
cortex_scaling_list = ['no']
pointstat = "classifscorezprobafullcortex"
thresholdtype = "pointstat"

hemispheres_list = ['rh','lh']
experiment = 'searchlight_HC_SZ'
for threshold in threshold_list:
	for n_scales in n_scales_list:
		for hem in hemispheres_list:
			for n_sl_points in n_sl_points_list:
				for cortex_scaling in cortex_scaling_list:
					#cmd = "frioul_batch 'python %s/11_multiscale_cluster_stats.py %s %s %s %d %d %.3f %d %s %s'" % (coderoot_dir, experiment, hem, graph_type, n_sl_points, n_permuts, threshold, n_scales, cortex_scaling, pointstat)
					#cmd = "qsub -cwd -q all.q -b y -V python %s/11_multiscale_cluster_stats.py %s %s %s %d %d %.3f %d %s %s" % (coderoot_dir, experiment, hem, graph_type, n_sl_points, n_permuts, threshold, n_scales, cortex_scaling, pointstat)
					cmd = "qsub -cwd -q all.q -b y -V -e /netapp/vol1_psy/basepsy/FS60/%s/log_files/loop11_%s_%s_errors.txt -o /netapp/vol1_psy/basepsy/FS60/%s/log_files/loop11_%s_%s_output.txt  python %s/11_multiscale_cluster_stats.py %s %s %s %d %d %.3f %d %s %s" % (experiment, hem, threshold, experiment, hem, threshold, coderoot_dir, experiment, hem, graph_type, n_sl_points, n_permuts, threshold, n_scales, cortex_scaling, pointstat)
					#a = commands.getoutput(cmd)
					a = subprocess.call(cmd, shell=True)
					print(cmd)
