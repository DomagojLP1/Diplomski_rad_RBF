import pandas as pd
import numpy as np
import os
from RBFNN.rbf import RBF
from RBF_with_AE.funcs import split_train_test
from RBF_with_AE.sort_with_acc import sort_with_acc
import pickle

only_delam=pd.read_csv(r'..\Data\processed_AE_data_v2\only_delamination.csv')
delam_data=pd.read_csv(r'..\Data\processed_AE_data_v2\delaminacija_data.csv')#all data
step_5_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_5_data.csv')
step_10_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_10_data.csv')
step_15_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_15_data.csv')
step_20_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_20_data.csv')
step_30_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_30_data.csv')
step_40_data=pd.read_csv(r'..\Data\processed_AE_data_v2\step_40_data.csv')

all_dfs=[delam_data,only_delam,step_5_data,step_10_data,step_15_data,step_20_data
         ,step_30_data,step_40_data]

for df in all_dfs: #drop unnecessary rows and columns
    df.drop(470,axis=0,inplace=True)
    df.drop(247,axis=0,inplace=True)
    df.drop(97,axis=0,inplace=True)
    df.reset_index(drop=True,inplace=True)
    df.drop(['name','uzorak','komad','fill','opseg','maxd'],axis=1,inplace=True)

S1,S2,S3,S4=[],[],[],[]
for row in range(only_delam['S'].size):
    if only_delam.iloc[row]['S']==1:
        S1.append(1)
        S2.append(0)
        S3.append(0)
        S4.append(0)
    elif only_delam.iloc[row]['S']==2:
        S1.append(0)
        S2.append(1)
        S3.append(0)
        S4.append(0)
    elif only_delam.iloc[row]['S'] == 3:
        S1.append(0)
        S2.append(0)
        S3.append(1)
        S4.append(0)
    elif only_delam.iloc[row]['S'] == 4:
        S1.append(0)
        S2.append(0)
        S3.append(0)
        S4.append(1)

keys = list(reversed(['S1', 'S2', 'S3','S4']))

values=[S1,S2,S3,S4]
values.reverse()
dict_s = dict(zip(keys, values))
for df in all_dfs: #NOW ALL dfs (step_10_data...) have s1 s2 s3 s4 and S + posmak, vc and all AE data
    for key, value in dict_s.items():
        df.insert(0,key,value)

step_dfs=[step_5_data,step_10_data,step_15_data,step_20_data,step_30_data,step_40_data]
step_dfs_names=['step_5_data','step_10_data','step_15_data','step_20_data','step_30_data','step_40_data']
# step_dfs=[step_5_data]


dict_accuracy={}
for i in range(len(step_dfs)):
    df=step_dfs[i]
    df_name=step_dfs_names[i]
    train_row=split_train_test(df)


    for col in [df.columns[z] for z in range(9,len(df.columns))]:
        train_df = df.iloc[train_row[col], :]
        test_row = [k for k in df.index.to_list() if k not in train_row[col]]
        test_df = df.iloc[test_row, :]
        

        train_out=train_df.loc[:,['S1', 'S2', 'S3','S4']]
        train_in=train_df.loc[:,['posmak','brzina_rezanja',col]]
        test_out=test_df.loc[:,['S1', 'S2', 'S3','S4']]
        test_in = test_df.loc[:,['posmak', 'brzina_rezanja', col]]

        test_in_val=test_in.values
        train_in_val=train_in.values
        test_out_val=test_out.values
        train_out_val=train_out.values

        for n in range(train_in_val.shape[1]):
            mx=np.max(train_in_val[:,n])
            train_in_val[:, n]=train_in_val[:,n]/mx
            test_in_val[:, n]=test_in_val[:,n]/mx


        rbf=RBF(train_in_val,train_out_val,test_in_val,test_out_val)

        accuracy=rbf.standard_out()[0]
        print('{}-{}-{}'.format(df_name, col,accuracy[0]))
        dict_accuracy.setdefault("{}".format(df_name), {}).setdefault(col,[]).append(accuracy[0])


#
with open(r'../Data/processed_AE_data_v2/dict_accuracy_one_feature.p', 'rb') as file:
    dict_accuracy = pickle.load(file)

features=sort_with_acc(dict_accuracy,0.25)


##TRAIN ALL good features
ls=['posmak','brzina_rezanja']
features_use=['S1', 'S2', 'S3','S4']+ls+features

df = delam_data[features_use].copy()
# df=delam_data
df_name='all'
# train_row=split_train_test(df)

# import random
# train_row=random.sample(range(0, df.shape[0]), 320)
# test_row=[k for k in df.index.to_list() if k not in train_row]

train_df = df.iloc[train_row, :]
test_df = df.iloc[test_row, :]

train_out=train_df.loc[:,['S1', 'S2', 'S3','S4']]
train_in=train_df.iloc[:,[o for o in range(9,df.shape[1])]]
test_out=test_df.loc[:,['S1', 'S2', 'S3','S4']]
test_in =test_df.iloc[:,[o for o in range(9,df.shape[1])]]

test_in_val=test_in.values
train_in_val=train_in.values
test_out_val=test_out.values
train_out_val=train_out.values

for n in range(train_in_val.shape[1]):
    mx=np.max(train_in_val[:,n])
    train_in_val[:, n]=train_in_val[:,n]/mx
    test_in_val[:, n]=test_in_val[:,n]/mx


rbf=RBF(train_in_val,train_out_val,test_in_val,test_out_val)

conf=rbf.standard_out()

print('{}-{}'.format(df_name,accuracy))









