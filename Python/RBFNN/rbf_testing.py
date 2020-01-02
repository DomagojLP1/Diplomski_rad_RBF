import pandas as pd
import numpy as np
# import os
import random

# test=pd.read_csv(r'C:\Users\Domagoj\Desktop\PYTHON PROJECTS\Diplomski\danko_rbf_test_data\test.csv',header=None)
# ucenje=pd.read_csv(r'C:\Users\Domagoj\Desktop\PYTHON PROJECTS\Diplomski\danko_rbf_test_data\ucenje.csv',header=None)
# output_cols=['2','3']
# input_cols=['0','1']
#
# ucenje_in=ucenje.iloc[:,[0,1]]
# ucenje_out=ucenje.iloc[:,[2,3]]
# test_in=test.iloc[:,[0,1]]
# test_out=test.iloc[:,[2,3]]
#
# ucenje_in=ucenje_in.values
# test_in=test_in.values

a=np.zeros([3,2])

ucenje_in=np.array([[5,1],[0,2],[-4,-7]])
ucenje_in=ucenje_in.astype(float)
a=ucenje_in.copy()
b=np.array([[5,1],[0,2],[-4,-7]])


for n in range(ucenje_in.shape[1]):
    max_val =np.max(ucenje_in[: ,n])
    ucenje_in[:, n ] =ucenje_in[: ,n ] /max_val

print(hex(id(a)))
print(hex(id(ucenje_in)))

a=