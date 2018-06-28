import pandas as pd 
import numpy as np 
import csv

def column_picker(df):
    
    # usecols = [*range(0,5),6]
    df = df['Totaal'].astype(float)
    # df_new = df.groupby('Dag').agg({'Dag':'first','Totaal':'sum'})
    

    # df.to_csv('gas_2009.csv',index=True)
    print(df.head())

     
df = pd.read_csv("dagprofielen gas.csv", sep=None, engine="python",skiprows=[0],decimal=",")
column_picker(df)