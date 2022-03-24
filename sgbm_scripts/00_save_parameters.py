import os
import os.path as op
import joblib


'''
Create two files in which we store i) the parameters used for extracting the pits and ii) the list of subjects and groups
'''

#Localisation du répertoire où l'on trouve les dossiers FS de nos sujets
root_analysis_dir = '/netapp/vol1_psy/basepsy/FS60'
#Nom du dossier qui sera créé dans le "root_analysis_dir"
experiment = 'searchlight_analysis'

#parameters used for the extraction of sulcal pits
alpha = '0.03'
an = '0'
dn = '20'
r = '1.5'
area = 50
param_string = 'D%sR%sA%s' % (dn,r,area)

#the subjects lists
pat = ['p0001', 'p0002', 'p0006']

ctrl = ['t0003', 't0009', 't0126']


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
