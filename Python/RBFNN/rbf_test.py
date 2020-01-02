import pandas as pd
import numpy as np
import os
from RBFNN.rbf import RBF

test=pd.read_csv(r'..\Data\danko_rbf_test_data\test_octave.csv',header=None)
ucenje=pd.read_csv(r'..\Data\danko_rbf_test_data\ucenje_octave.csv',header=None)

output_cols=['2','3']
input_cols=['0','1']
# ucenje=ucenje.to_numpy()
# hidden_neurons=ucenje[:,[0,1]]
# ucenje_in=hidden_neurons
# ucenje_out=ucenje[:,[2,3]]
# test=test.to_numpy()
# test_in=test[:,[0,1]]
# test_out=test[:,[2,3]]

ucenje_in=ucenje.iloc[:,[0,1]]
ucenje_out=ucenje.iloc[:,[2,3]]
test_in=test.iloc[:,[0,1]]
test_out=test.iloc[:,[2,3]]

print(1)
rbf=RBF(ucenje_in,ucenje_out,test_in,test_out,koef=2,normalization=0)
print(2)
accuracy,confusion_mat,total,result,krivi,C,sigmas,hidden,rbf_out,rbf_out_raw=rbf.standard_out()