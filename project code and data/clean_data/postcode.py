import pandas as pd 
import numpy as np 

def postcode_select(df):
    
    df['begin_POST'] = df['POSTCODE_TOT'].astype(str).str[0:4]
    d = {'STRAATNAAM': 'first','Aantal Aansluitingen':'sum','%Fysieke status':'mean','SJV':'sum'}
    df_new = df.groupby('begin_POST').aggregate(d)
    df_new.to_csv('group_kvg_2009.csv')

    # print(df_new.shape)

    # print(df_new.head())

df = pd.read_csv('kvg_2009.csv', sep=None,decimal=",", engine="python")

postcode_select(df)