import os
import numpy as np
import pandas as pd
from scipy import integrate
import matplotlib.pyplot as plt
import math

delaminacija_data=pd.read_csv('../Data/processed_AE_data_v2/delaminacija_data.csv')
stupci=delaminacija_data.columns

only_start=delaminacija_data.loc[:,'name':'avgd']
step_5=delaminacija_data.loc[:,'50-55':'395-400']
step_10=delaminacija_data.loc[:,'50-60':'390-400']
step_15=delaminacija_data.loc[:,'50-65':'380-395']
step_20=delaminacija_data.loc[:,'50-70':'370-390']
step_30=delaminacija_data.loc[:,'50-80':'380-400']
step_40=delaminacija_data.loc[:,'50-90':'370-400']

step_5_data=pd.concat([only_start,step_5],axis=1)
step_10_data=pd.concat([only_start,step_10],axis=1)
step_15_data=pd.concat([only_start,step_15],axis=1)
step_20_data=pd.concat([only_start,step_20],axis=1)
step_30_data=pd.concat([only_start,step_30],axis=1)
step_40_data=pd.concat([only_start,step_40],axis=1)

only_start.to_csv('only_delamination.csv',index=False)
step_5_data.to_csv('step_5_data.csv',index=False)
step_10_data.to_csv('step_10_data.csv',index=False)
step_15_data.to_csv('step_15_data.csv',index=False)
step_20_data.to_csv('step_20_data.csv',index=False)
step_30_data.to_csv('step_30_data.csv',index=False)
step_40_data.to_csv('step_40_data.csv',index=False)
