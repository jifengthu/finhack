import sys
import os
import time
import random
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from library.astock import AStock
from factors.indicatorCompute import indicatorCompute
from library.mydb import mydb
from library.globalvar import *
import pandas as pd
import pickle


index_list=mydb.selectToDf("select con_code from astock_index_weight where ts_code='000852.SH'",'tushare')
index_list=list(set(index_list['con_code'].to_list()))
#print(index_list)


model_hash="3d7f01c6a3f25143029533c904efe7a8"

pkl_file="/data/code/finhack/data/preds/lgb_model_"+model_hash+"_pred.pkl"
with open(pkl_file,'rb') as f:
    df=pickle.load(f)
    df = df[df['ts_code'].isin(index_list)]
    df=df.reset_index(drop=True)
    df.to_csv(pkl_file+".csv")
    


    
    
print(df)





print("scp -P30022 woldy@woldy.net:/data/code/finhack/data/preds/lgb_model_"+model_hash+"_pred.pkl.csv ~/Downloads/")