import pandas as pd 
import numpy as np 
import csv

def column_picker(df):
    
    # usecols = [*range(0,5),6]
    
    # d = {'Totaal':'sum'}
    df['DAG'] = df['Dag'].astype(float)
    # df_new = df.groupby('DAG').aggregate(d)
    

    df_new = df.groupby('DAG').agg({'Dag':'first','Totaal':'sum'})
    # df_new = df_new['DAG']
    
    # conditions = (df["WOONPLAATS"] == "AMSTERDAM")|(df["WOONPLAATS"] == "AMSTERDAM ZUIDOOST")|(df["WOONPLAATS"] == "AMSTERDAM ZUID00ST")
    # df = df.loc[conditions]
    # df = df.drop('WOONPLAATS',axis=1)
    df_new.to_csv('elk_2009.csv',index=False)
    # print(df_new.head())


df = pd.read_csv("dagprofielen elektriciteit.csv", sep=None, engine="python",skiprows=[0],decimal=",",usecols=[0,1,4])
column_picker(df)