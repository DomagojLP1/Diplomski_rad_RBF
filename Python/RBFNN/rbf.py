import pandas as pd
import numpy as np
import random



class RBF:
    def __init__(self,train_in,train_out,test_in,test_out,koef=1,normalization=1):
        self.train_in=train_in
        self.train_out=train_out
        self.test_in=test_in
        self.test_out=test_out
        self.koef=koef

        self.to_normalize=normalization

        if isinstance(self.train_in,pd.DataFrame):
            self.train_in_df=self.train_in
            self.train_in=self.train_in_df.values.copy()
            self.train_out_df=self.train_out
            self.train_out=self.train_out_df.values.copy()
            self.test_in_df=self.test_in
            self.test_in=self.test_in_df.values.copy()
            self.test_out_df=self.test_out
            self.test_out=self.test_out_df.values.copy()


        
    @staticmethod    
    def activation(sigma,dist):
        return np.exp(-(dist/sigma)**2)

    def normalization(self):
        self.max_values=[]
        for n in range(self.train_in.shape[1]):
            max_val=np.max(self.train_in[:,n])
            self.train_in[:, n]=self.train_in[:,n]/max_val
            self.test_in[:, n]=self.test_in[:,n]/max_val
            self.max_values.append(max_val)


    def training(self):
        hidden=self.train_in
        distance=np.zeros([self.train_in.shape[0],hidden.shape[0]])
        for neuron in range(distance.shape[1]):
            for sample in range(distance.shape[0]):
                distance[sample,neuron]=np.linalg.norm(np.subtract(self.train_in[sample],hidden[neuron]))
        
        sigmas=[]        
        for neuron_col in range(hidden.shape[0]):
            neuron=hidden[neuron_col]
            dist=[]
            for i in range(hidden.shape[0]):
                dist.append(np.linalg.norm(np.subtract(hidden[i],neuron)))
            mins=[sorted(dist)[1],sorted(dist)[2]]#takes second and third argument for miniminal distance since the first one is 0 because it is comparing with the same neuron
            sigmas.append(self.koef*np.sqrt(mins[0]*mins[1]))
            
            
        H=np.zeros(distance.shape)            
        for neuron in range(H.shape[1]):
            for sample in range(H.shape[0]):
                H[sample,neuron]=self.activation(sigmas[neuron],distance[sample,neuron])
        C=np.matmul(np.linalg.pinv(H),self.train_out)
        return C,sigmas,hidden
        
    
    def test(self,C,sigmas,hidden):
        distance_test=np.zeros([self.test_in.shape[0],hidden.shape[0]])
        for neuron in range(distance_test.shape[1]):
            for sample in range(distance_test.shape[0]):
                distance_test[sample,neuron]=np.linalg.norm(np.subtract(self.test_in[sample],hidden[neuron]))
        Ht=np.zeros(distance_test.shape)
        for neuron in range(Ht.shape[1]):
            for sample in range(Ht.shape[0]):
                Ht[sample,neuron]=self.activation(sigmas[neuron],distance_test[sample,neuron])        
        rbf_out_raw=np.matmul(Ht,C)
        rbf_out=np.zeros(rbf_out_raw.shape)
        for i in range(rbf_out.shape[0]):
            loc=np.argmax(rbf_out_raw[i,:])
            out=np.zeros(rbf_out.shape[1])
            out[loc]=1
            rbf_out[i,:]=out.copy()

            # for j in range(rbf_out.shape[1]): ### način gdje rounda i sve mora biti točno
            #     rbf_out[i,j]=round(rbf_out_raw[i,j])


        return rbf_out,rbf_out_raw
    
    def check_output(self,rbf_out):
        result=np.zeros([self.test_out.shape[0],1])
        krivi=[]
        for i in range(self.test_out.shape[0]):

            if np.array_equal(self.test_out[i], rbf_out[i]):
                result[i,0]=True
            else:
                result[i,0]=False
                krivi.append(i)
        total_corr=sum(result)
        total=len(result)        
        accuracy=total_corr/total
        
        return accuracy,total_corr,total,result,krivi

    def confusion_matrix(self,rbf_out):
        cols=['name','ps1','ps2','ps3','ps4','sum']
        dct=dict((col,[0 for i in range(5)]) for col in cols)

        for row in range(rbf_out.shape[0]):
            for columna in range(rbf_out.shape[1]):
                for columnp in range(rbf_out.shape[1]):
                    if rbf_out[row, columnp] == 1 and self.test_out[row, columna] == 1:
                        dct[cols[columnp + 1]][columna] = dct[cols[columnp + 1]][columna] +1

        confusion_mat = pd.DataFrame().from_dict(dct)
        confusion_mat.loc[:, 'name'] = ['as1', 'as2', 'as3', 'as4', 'sum']
        return confusion_mat

    def standard_out(self):
        if self.to_normalize==1:
            self.normalization()
        C,sigmas,hidden=self.training()
        rbf_out,rbf_out_raw=self.test(C,sigmas,hidden)
        accuracy,total_corr,total,result,krivi=self.check_output(rbf_out)
        confusion_mat=self.confusion_matrix(rbf_out)
        return accuracy,confusion_mat,total,result,krivi,C,sigmas,hidden,rbf_out,rbf_out_raw
        
