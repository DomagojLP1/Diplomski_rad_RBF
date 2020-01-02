# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:15:39 2019

@author: Domagoj
"""

import pandas as pd
import numpy as np
import os


    

test=pd.read_csv('test.csv',header=None)
ucenje=pd.read_csv('ucenje.csv',header=None)

        
output_cols=['2','3']
input_cols=['0','1']
ucenje=ucenje.to_numpy()
hidden_neurons=ucenje[:,[0,1]]
ucenje_in=hidden_neurons
ucenje_out=ucenje[:,[2,3]]
test=test.to_numpy()
test_in=test[:,[0,1]]
test_out=test[:,[2,3]]

def activation(sigma,dist):
    return np.exp(-(dist/sigma)**2)

goodness=[]

for koef in [2]:
    distance=np.zeros([hidden_neurons.shape[0],hidden_neurons.shape[0]])
    
    for neuron in range(distance.shape[1]):
        for sample in range(distance.shape[0]):
            distance[sample,neuron]=np.linalg.norm(ucenje_in[sample],hidden_neurons[neuron])