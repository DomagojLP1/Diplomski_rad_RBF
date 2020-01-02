import numpy as np
import pandas as pd

def split_train_test(df):
    f=[i for i in df['posmak'].unique() if i!=0]
    vc=[i for i in df['brzina_rezanja'].unique() if i!=0]
    s=[i for i in df['S'].unique() if i!=0]

    cols=df.columns
    train_row_dict={}
    train_row_dict.fromkeys(cols[9:],[])

    for col in [cols[i] for i in range(9,len(cols))]: #9 because the wanted columns start from 9
        for s1 in s:
            for f1 in f:
                for vc1 in vc:
                    filtered=df.loc[(df['posmak']==f1) & (df['brzina_rezanja']==vc1)& (df['S']==s1)][col]
                    train_num=int(filtered.shape[0]/2+0.5)
                    # test_num=filtered.shape[0]/2-train_num
                    train_rows,dists=get_test_train_rows(filtered,train_num)
                    train_row_dict.setdefault(col,[]).extend(train_rows)


    return train_row_dict


def get_test_train_rows(filtered,train_num):
    """
    filtered= filtrirani DF
    train_num=broj uzoraka za train
    output test_rows = najblizi meanu, i train_num-1 najdaljih od meana
    dists=izracunate udaljenosti po redu


    :param filtered:
    :param test_num:
    :return test_rows, dists:
    """
    data=filtered
    mean=np.mean(data)
    dists=[]
    for i in range(filtered.shape[0]):
        dists.append(abs(filtered.iloc[i]-mean))

    dists_enum=list(enumerate(dists))
    dists_enum.sort(key=lambda x: x[1])

    train_rows=[]
    train_rows.append(dists_enum[0][0])
    dists_enum_rever=list(reversed(dists_enum))
    for i in range(train_num-1):
        train_rows.append(dists_enum_rever[i][0])
    train_rows = [x + data.index[0] for x in train_rows]

    return train_rows,dists












