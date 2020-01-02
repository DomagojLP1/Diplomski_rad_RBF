from oct2py import octave
from oct2py import Oct2Py
import os
import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import math
from decimal import Decimal
import ctypes

path_slike=r"e:\DIPLOMSKI2019\indirektna\Slike_delminacije\DU"

def make_hole_names():
    """
    Daje dictionary sa imenima svih rupa tipa D6d0S1-F0d09-Vc45-MJ001-K01 sa vrijednostima tipa :['D6d0S2', 'F0d03', 'Vc45', 'MJ010', 'K20']
    Daje dataframe od tog dictionarya
    :return:
    """
    rupe={}
    svi_podaci=os.listdir(r"e:\DIPLOMSKI2019\Diplomski112019\Indirektna mjerenja")
    for i in svi_podaci:
        a=os.path.splitext(i)[0].split('-')
        b='-'.join(a[0:-1])
        if a[5]=='ae':
            rupe[b]=a[0:-1]

        for key, value in rupe.items():
            rupe[key][2]=rupe[key][2][:4]

    names_df=pd.DataFrame(rupe)

    return names_df

def read_AE(folder_path,rupe_df):
    oc = Oct2Py()
    steps = [5, 10, 15, 20, 30, 40]  # in khz
    AE_data_dict = {'name': []}
    for step in steps:
        for i in range(math.ceil(350/step)):
            start=50+i*step
            end=50+step+i*step
            if end>400:
                end=400
            AE_data_dict['{}-{}'.format(int(start),int(end))]=[]
    #r'e:\DIPLOMSKI2019\Diplomski112019\Indirektna mjerenja'
    for column in rupe_df.columns:
        AE_data=process_AE(pd.read_csv(folder_path+'\\'+column+'-ae.txt',squeeze=True).values.tolist(), oc)

        ime_split=column.split('-')
        novo_ime='-'.join([ime_split[0],ime_split[1],ime_split[2][0:4],ime_split[3],ime_split[4]])
        AE_data_dict['name'].append(novo_ime)
        for key in AE_data:
            AE_data_dict[key].append(AE_data[key])
        print(column)

    # for key in AE_data_dict.keys():
    #     if key!='name':
    #         AE_data_dict[key]=AE_data_dict[key][0]
    rupe_AE_df=pd.DataFrame.from_dict(AE_data_dict)
    return rupe_AE_df

def process_AE(data,oc):

    steps=[5,10,15,20,30,40] # in khz
    hz_from_to=[50,400] #in khz
    AE_data={}

    frekv, ampl, power = run_ftran_octave(data,oc)
    power = np.transpose(power)
    for step in steps:
        start=50
        for i in range(math.ceil(350/step)):
            start=50+i*step
            end=50+step+i*step
            if end>400:
                end=400
            # simpsons_area=integrate.simps(frekv[start:end+1], power[start:end]+1)

            start_index=np.where(frekv == start*1000)[0][0]
            end_index=np.where(frekv == end*1000)[0][0]

            trap_area=trap_area_calc(frekv[start_index:end_index+1], power[start_index:end_index+1])

            # AE_data['simpsons_area'] = simpsons_area;
            AE_data['{}-{}'.format(int(start),int(end))]=trap_area[0]


    return AE_data

def trap_area_calc(x,y):

    area=np.sum(y)*(x[-1]-x[0])/y.size
    return area

def run_ftran_octave(data_in,oc):

    [frekv, ampl, power]=oc.ftran(data_in,0.1,nout=3)
    return frekv, ampl, power


rupe_df=make_hole_names()
rupe_AE_df=read_AE(r'e:\DIPLOMSKI2019\Diplomski112019\Indirektna mjerenja',rupe_df)
ctypes.windll.user32.MessageBoxW(0, "Script finished", "Finished", 1)
rupe_AE_df.to_csv('rupe_AE_v2.csv')

# ff=read_AE(r'e:\DIPLOMSKI2019\Diplomski112019\Indirektna mjerenja',rupe_df.iloc[:,[0,1]])

