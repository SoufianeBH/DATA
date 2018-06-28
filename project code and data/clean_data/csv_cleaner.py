import pandas as pd 
import numpy as np 
import csv

def column_picker(df):
    

    conditions = (df["WOONPLAATS"] == "AMSTERDAM")|(df["WOONPLAATS"] == "AMSTERDAM ZUIDOOST")|(df["WOONPLAATS"] == "AMSTERDAM ZUID00ST")
    df = df.loc[conditions]
    df = df.drop('WOONPLAATS',axis=1)
    # df['begin_POST'] = df['POSTCODE_VAN'].astype(str).str[0:4]
    df.to_csv('kvg_2016.csv',index=False)

usecols = [*range(3,7),8,*range(10,13),16,17]
df = pd.read_csv("Liander_kleinverbruiksgegevens_01012016.csv", sep=None, decimal=",", engine="python",usecols=usecols)

column_picker(df)



# Liander_kleinverbruiksgegevens_01012009.csv
# Liander_kleinverbruiksgegevens_01012015.csv
# Liander_kleinverbruiksgegevens_01012016.csv