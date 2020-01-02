import os
import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import math

delaminacija=pd.read_csv(r'../Data/delamination_data/Delaminacija.csv')
rupe_AE=pd.read_csv(r'../Data/AE_data/rupe_AE_v2.csv')


ve={'S':[],'posmak':[],'brzina_rezanja':[],'uzorak':[],'komad':[],'fill':[],'split':[],'opseg':[],'maxd':[],'avgd':[]}
ve_keys=list(ve.keys())


for key in reversed(ve_keys):
    rupe_AE.insert(2,key,pd.Series([0 for i in range(rupe_AE['name'].size)]))

for name in delaminacija['name']:
    index=delaminacija.loc[delaminacija['name'] == name].index.values.astype(int)[0]
    ime_split=name.split('-')
    novo_ime='-'.join([ime_split[0],ime_split[1],ime_split[2][0:4],ime_split[3],ime_split[4]])
    delaminacija.loc[index,'name']=novo_ime


rupe_AE['S']=[0 for i in range(rupe_AE['S'].size)]

for name in rupe_AE['name']:
    for key in ve_keys:
        try:
            rupe_AE.loc[rupe_AE['name']==name,key]=delaminacija.loc[delaminacija['name'] == name,key].values[0]
        except IndexError:
            print('Rupa {} ne postoji'.format(name))
            rupe_AE.loc[rupe_AE['name'] == name, key]=0

rupe_AE=rupe_AE.drop(rupe_AE.columns[0],1)

delaminacija.sort_values(by=['name'])
rupe_AE.sort_values(by=['name'])


"""IF floats are in list and viewed as string, this casts it to float"""
# for column in rupe_AE.columns:
#     try:
#         rupe_AE[column]=rupe_AE[column].str.strip('[]').astype(float)
#     except:
#        pass


delaminacija_data=rupe_AE
delaminacija_data.to_csv(r'..\Data\processed_AE_data_v2\delaminacija_data.csv',index=False)
# delaminacija_sve=pd.DataFrame()