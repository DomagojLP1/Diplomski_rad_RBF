import os
import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


delam=pd.read_csv('only_delamination.csv')
delam_sort=pd.read_csv('Delaminacija_sort.csv',delimiter=';')

for i in range(delam['S'].size):
    if (delam.loc[i,'S']==1) or (delam.loc[i,'S']==2) :
        delam.loc[i, 'S']=1
    else:
        delam.loc[i, 'S']=2

for name in delam_sort['Slika']:
    index=delam_sort.loc[delam_sort['Slika'] == name].index.values.astype(int)[0]
    ime_split=name.split('-')
    novo_ime='-'.join([ime_split[0],ime_split[1],ime_split[2][0:4],ime_split[3],ime_split[4][0:3]])
    delam_sort.loc[index,'Slika']=novo_ime

delam_sort=delam_sort.fillna(0.0)

delam_sort_no_both=delam_sort[(delam_sort['Izbaciti'] == float(1.00000))|(delam_sort['Previse Mrlja'] == float(1.00000))]

delam_sort_no_izbaciti=delam_sort[delam_sort['Izbaciti'] == float(1.000000)]

delam_sort_no_all=delam_sort[(delam_sort['Izbaciti'] == float(1.00000))|(delam_sort['Previse Mrlja'] == float(1.00000))|(delam_sort['Dosta Mrlja'] == float(1.00000))]



stupci=['fill','split', 'opseg', 'maxd', 'avgd']
column_names=['brzina_rezanja','posmak','S']
S=[1,2,3,4]
posmak=[0.03000,0.06000,0.09000,0.12000]
brzina_rezanja=[15.000000,30.000000,45.000000,60.000000]
# df.loc[df['column_name'] == some_value]


dict_stupci={key: [] for key in stupci}
average_data={'s1':{},'s2':{},'s3':{},'s4':{}}
for i in stupci:
        for key in average_data:
            average_data[key].update({i:{}})

for i in posmak:
    for j in brzina_rezanja:
        for key in average_data:
            for key1 in average_data[key]:
                average_data[key][key1].update({str(i)+'-'+str(j):[]})
"""TU smo dobili dictionary average data
average_data
    s1 s2 s3 s4
        fill split opseg maxd avgd
            0.03-15.0...
"""#Readme za nested dicts
for s in S:
    for p in posmak:
        for br in brzina_rezanja:
            a=delam.loc[delam['brzina_rezanja']==br]
            b=a.loc[a['posmak']==p]
            c=b.loc[b['S']==s].reset_index()

            c=c.loc[~c['name'].isin(delam_sort_no_izbaciti['Slika'])]

            for stupac in stupci:
                average_data['s'+str(s)][stupac][str(p)+'-'+str(br)]=c[stupac].sum()/(c[stupac].size-c[stupac].isna().sum())

X = np.arange(0.03, 0.15, 0.03)
Y = np.arange(15.0, 75.0, 15.0)
X, Y = np.meshgrid(X, Y)

z=np.reshape(list(average_data['s1']['fill'].values()),(4,4))
z1=np.reshape(list(average_data['s2']['fill'].values()),(4,4))
# z2=np.reshape(list(average_data['s3']['avgd'].values()),(4,4))
# z3=np.reshape(list(average_data['s4']['avgd'].values()),(4,4))


fig = plt.figure()
ax = Axes3D(fig)
surf=ax.plot_surface(X,Y,z,label='s1',alpha=1)
surf._facecolors2d=surf._facecolors3d
surf._edgecolors2d=surf._edgecolors3d
surf=ax.plot_surface(X,Y,z1,label='s2',alpha=1)
surf._facecolors2d=surf._facecolors3d
surf._edgecolors2d=surf._edgecolors3d
# surf=ax.plot_surface(X,Y,z2,label='s3',alpha=1)
# surf._facecolors2d=surf._facecolors3d
# surf._edgecolors2d=surf._edgecolors3d
# surf=ax.plot_surface(X,Y,z3,label='s4',alpha=1)
# surf._facecolors2d=surf._facecolors3d
# surf._edgecolors2d=surf._edgecolors3d


fig.legend()





"""
PRIJAŠNJI NAČIN GDJE JE BIO SAMO JEDAN DICT
for s in S:
    for p in posmak:
        for br in brzina_rezanja:
            a=delam.loc[delam['brzina_rezanja']==br]
            b=a.loc[a['posmak']==p]
            c=b.loc[b['S']==s]
            for stupac in stupci:
                average_data[str(s)+'-'+str(p)+'-'+str(br)+'-'+stupac]=c[stupac].sum()/(c[stupac].size-c[stupac].isna().sum())

"""#samo jedan dict