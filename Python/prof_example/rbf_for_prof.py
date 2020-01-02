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
            distance[sample,neuron]=np.linalg.norm(np.subtract(ucenje_in[sample],hidden_neurons[neuron]))
            
    
    
    
    sigmas=[]
    zers=[]
    for neuron_col in range(hidden_neurons.shape[0]):
        neuron=hidden_neurons[neuron_col]
        dist=[]
        for i in range(hidden_neurons.shape[0]):
            dist.append(np.linalg.norm(np.subtract(hidden_neurons[i],neuron)))
        zer=[sorted(dist)[0]]
        smalls=[sorted(dist)[1],sorted(dist)[2]]
        sigmas.append(koef*np.sqrt(smalls[0]*smalls[1]))
        zers.append(zer)
    
    
    H=np.zeros([hidden_neurons.shape[0],hidden_neurons.shape[0]])
    for neuron in range(H.shape[1]):
        for sample in range(H.shape[0]):
            H[sample,neuron]=activation(sigmas[neuron],distance[sample,neuron])
    C=np.matmul(np.linalg.pinv(H),ucenje_out)
                                             
    
    
    distance_test=np.zeros([test_in.shape[0],hidden_neurons.shape[0]])
    for neuron in range(distance_test.shape[1]):
        for sample in range(distance_test.shape[0]):
            distance_test[sample,neuron]=np.linalg.norm(np.subtract(test_in[sample],hidden_neurons[neuron]))
    Ht=np.zeros(distance_test.shape)
    for neuron in range(Ht.shape[1]):
        for sample in range(Ht.shape[0]):
            Ht[sample,neuron]=activation(sigmas[neuron],distance_test[sample,neuron])
    out=np.matmul(Ht,C)
    out_f=[]
    for i in range(out.shape[0]):
        if out[i,0]>out[i,1]:
            out_f.append(0)
        else:
            out_f.append(1)
    test_out_f=[]       
    for i in range(test_out.shape[0]):
        if test_out[i,0]>test_out[i,1]:
            test_out_f.append(0)
        else:
            test_out_f.append(1) 
    goodness_counter=0        
    for i in range(test_out.shape[0]):
        if out_f[i]==test_out_f[i]:
            goodness_counter=goodness_counter+1
    goodness.append(goodness_counter)
    
            
        


