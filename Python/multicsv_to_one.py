import os
import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import math


sve={'name':[],'S':[],'posmak':[],'brzina_rezanja':[],'uzorak':[],'komad':[],'fill':[],'split':[],'opseg':[],'maxd':[],'avgd':[]}
what=os.listdir(os.path.join(os.getcwd(),'csv'))
for file in what:
    a=file.split('-')
    b=a[3].split('_')[0]
    # sve['-'.join([a[1],a[2],b])]=pd.read_csv(os.path.join(os.getcwd(),'csv',file))
    # a=pd.read_csv(os.path.join(os.getcwd(),'csv',file))
    for index, row in pd.read_csv(os.path.join(os.getcwd(),'csv',file)).iterrows():
        sve['name'].append(row['Sketch'][0:-3])
        sve['S'].append(row['Sx'])
        sve['posmak'].append(row['Posmak'])
        sve['brzina_rezanja'].append(row['Brzina_rezanja'])
        sve['uzorak'].append(row['Uzorak'])
        sve['komad'].append(row['Mjerenje'][0:-3])
        sve['fill'].append(row['Fill_Povrsina'])
        sve['split'].append(row['Split_povrsina'])
        sve['opseg'].append(row['Opseg_delminacije'])
        sve['maxd'].append(row['MaxD'])
        sve['avgd'].append(row['AvgD'])

Delaminacija_df=pd.DataFrame(sve)
Delaminacija_df.to_csv('Delaminacija.csv')