import os
import os.path as op
import joblib


'''
Create two files in which we store i) the parameters used for extracting the pits and ii) the list of subjects and groups
'''

#Localisation du répertoire où l'on trouve les dossiers FS de nos sujets
root_analysis_dir = '/netapp/vol1_psy/basepsy/FS60'
#Nom du dossier qui sera créé dans le "root_analysis_dir"
experiment = 'searchlight_HC_SZ_radius_50'

#parameters used for the extraction of sulcal pits
alpha = '0.03'
an = '0'
dn = '20'
r = '1.5'
area = 50
param_string = 'D%sR%sA%s' % (dn,r,area)

#the subjects lists
pat = ['p0001', 'p0002', 'p0006', 'p0008', 'p0009', 'p0013', 'p0015', 'p0020', 'p0025', 'p0031', 'p0035', 'p0036', 'p0060', 'p0064', 'p0065', 'p0066', 'p0068', 'p0069', 'p0070', 'p0071', 'p0072', 'p0077', 'p0078', 'p0081', 'p0082', 'p0083', 'p0084', 'p0085', 'p0086', 'p0087', 'p0088', 'p0090',	'p0092', 'p0093', 'p0095', 'p0096',	'p0098', 'p0099', 'p0100', 'p0101', 'p0102', 'p0103', 'p0104', 'p0105', 'p0106', 'p0109', 'p0110', 'p0111', 'p0112', 'p0114', 'p0118', 'p0120', 'p0123', 'p0124',	'p0126', 'p0127', 'p0128', 'p0129', 'p0130', 'p0131', 'p0132', 'p0133', 'p0134', 'p0135', 'p0136', 'p0137', 'p0138', 'p0140', 'p0141', 'p0144', 'p0148', 'p0151', 'p0154']

ctrl = ['t0003', 't0009', 't0126', 't0148', 't0174', 't0175', 't0253', 't0271', 't0278', 't0290', 't0335', 't0340', 't0353', 't0355', 't0356', 't0358', 't0359', 't0363', 't0364', 't0376', 't0402', 't0404', 't0408', 't0468', 't0487', 't0488', 't0490', 't0497', 't0501', 't0508', 't0523', 't0548', 't0549', 't0550', 't0551', 't0560', 't0562', 't0566', 't0575', 't0593', 't0594', 't0595', 't0625', 't0629', 't0633', 't0643', 't0677', 't0685', 't0686', 't0703', 't0704', 't0710', 't0713', 't0739', 't0740', 't0743', 't0745', 't0746', 't0747', 't0748', 't0749', 't0750', 't0751', 't0752', 't0753', 't0754', 't0755', 't0756', 't0757', 't0758', 't0760', 't0761', 't0764', 't0765', 't0766', 't0768', 't0769', 't0770', 't0771', 't0772', 't0773', 't0774', 't0775', 't0776', 't0777', 't0778', 't0779', 't0780', 't0781', 't0782', 't0783', 't0784', 't0785', 't0786', 't0788', 't0806', 't0807', 't0808', 't0809', 't0810']


groups_list = []
groups_list.append(pat)
groups_list.append(ctrl)

groupnames_list = ['pat','ctrl']

subjects_list = []
for group in groups_list:
    subjects_list.extend(group)


#create directory where all the analyses will be performed
analysis_dir = op.join(root_analysis_dir, experiment)
try:
    os.makedirs(analysis_dir)
    print('Creating new directory: %s' % analysis_dir)
except:
    print('Output directory is %s' % analysis_dir)


subjectslist_path = op.join(analysis_dir,'subjects_list.jl')
joblib.dump([groups_list, subjects_list],subjectslist_path,compress=3)


params_path = op.join(analysis_dir,'pits_extraction_parameters.jl')
joblib.dump([alpha, an, dn, r, area, param_string],params_path,compress=3)


#create labels y and other variables
y = []
samples_hem_list = []
samples_group_list = []
samples_subjects_list = []
for group_ind in range(len(groups_list)):
    for subject in groups_list[group_ind]:
        y.append(group_ind)
        samples_hem_list.append('')
        samples_group_list.append(groupnames_list[group_ind])
        samples_subjects_list.append(subject)

sampleslist_path = op.join(analysis_dir,'samples_list.jl')
joblib.dump([y, samples_subjects_list, samples_hem_list, samples_group_list],sampleslist_path,compress=3)
