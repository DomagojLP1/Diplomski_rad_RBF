import pickle
import pandas as pd

def sort_with_acc(dict_acc,limit,path=False):
    """
    r'../Data/processed_AE_data_v2/dict_accuracy_one_feature.p','rb'
    """
    if path==True:
        with open(dict_acc,'rb') as file:
            dict_acc=pickle.load(file)

    dict_range_acc={'start':[],'end':[],'acc':[]}
    for key_step in dict_acc:
        for key_range, value in dict_acc[key_step].items():
            nums=key_range.split('-')
            startnum=int(nums[0])
            endnum=int(nums[1])
            dict_range_acc['start'].append(startnum)
            dict_range_acc['end'].append(endnum)
            dict_range_acc['acc'].append(value[0])

    dict_acc_df=pd.DataFrame.from_dict(dict_range_acc)


    sorted_df=dict_acc_df.sort_values(by=['acc'],ascending=False).reset_index(drop=True)
    last=None

    #find the row of the last value that has required acc
    for i in range(sorted_df['acc'].size):
        if sorted_df.iloc[i]['acc']<limit and last == None:
            last=i ##
    sorted_df_grtr=sorted_df.iloc[0:last,:]
    sorted_df_grtr_np=sorted_df_grtr.to_numpy()

    izbaciti=[]
    for i in range(sorted_df_grtr_np.shape[0]):
        start=sorted_df_grtr_np[i,0]
        end=sorted_df_grtr_np[i,1]
        if i!=sorted_df_grtr_np.shape[0]-1:
            for j in range(i+1,sorted_df_grtr_np.shape[0]):
                startj = sorted_df_grtr_np[j, 0]
                endj = sorted_df_grtr_np[j, 1]
                if startj>start and endj<end:
                    izbaciti.append('{}-{}'.format(int(startj),int(endj)))

    uzeti=[]
    for i in range(sorted_df_grtr_np.shape[0]):
        start=sorted_df_grtr_np[i,0]
        end=sorted_df_grtr_np[i,1]
        c='{}-{}'.format(int(start),int(end))
        if c not in izbaciti:
            uzeti.append(c)

    return uzeti


if __name__ == "__main__":
    a=sort_with_acc(r'../Data/processed_AE_data_v2/dict_accuracy_one_feature.p', 0.3, path=True)






