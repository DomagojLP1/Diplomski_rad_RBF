import pandas as pd
import numpy as np
import os
import random
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

from RBFNN import rbf

only_delam=pd.read_csv(r'..\Data\processed_AE_data_v2\only_delamination.csv')
delam_data=pd.read_csv(r'..\Data\processed_AE_data_v2\delaminacija_data.csv')#all data
step_5_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_5_data.csv')
step_10_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_10_data.csv')
step_15_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_15_data.csv')
step_20_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_20_data.csv')
step_30_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_30_data.csv')
step_40_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_40_data.csv')

all_dfs=[only_delam,step_5_data,step_10_data,step_15_data,step_20_data
         ,step_30_data,step_40_data]

for df in all_dfs:
    df.drop(470,axis=0,inplace=True)
    df.drop(247,axis=0,inplace=True)
    df.drop(97,axis=0,inplace=True)
    df.reset_index(drop=True,inplace=True)
    df.drop(['name','uzorak','komad'],axis=1,inplace=True)


# only_delam_rbf=only_delam.drop(['name','uzorak','komad'],axis=1)
# step_5_rbf=step_5_data.drop(['name','uzorak','komad'],axis=1)
# step_10_rbf=step_10_data.drop(['name','uzorak','komad'],axis=1)
# step_15_rbf=step_15_data.drop(['name','uzorak','komad'],axis=1)
# step_20_rbf=step_20_data.drop(['name','uzorak','komad'],axis=1)
# step_30_rbf=step_30_data.drop(['name','uzorak','komad'],axis=1)
# step_40_rbf=step_40_data.drop(['name','uzorak','komad'],axis=1)

a=rbf(only_delam,delam_data)
a.standard_out()

# =============================================================================
# step_5_norm=preprocessing.normalize(step_5_rbf,axis=0,norm='max')
# step_10_norm=preprocessing.normalize(step_10_rbf,axis=0,norm='max')
# step_15_norm=preprocessing.normalize(step_15_rbf,axis=0,norm='max')
# step_20_norm=preprocessing.normalize(step_20_rbf,axis=0,norm='max')
# step_30_norm=preprocessing.normalize(step_30_rbf,axis=0,norm='max')
# step_40_norm=preprocessing.normalize(step_40_rbf,axis=0,norm='max')
# =============================================================================



    
    
    
        
    
    
