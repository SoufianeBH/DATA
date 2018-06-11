import pandas as pd 
import numpy as np 
import csv

def column_picker(csv_file):
    
    usecols = [*range(3,7),8,*range(10,13),16,17]
    df = pd.read_csv(csv_file, sep=None, engine="python",usecols=usecols)

    conditions = (df["WOONPLAATS"] == "AMSTERDAM")|(df["WOONPLAATS"] == "AMSTERDAM ZUIDOOST")|(df["WOONPLAATS"] == "AMSTERDAM ZUID00ST")
    df = df.loc[conditions]
    df = df.drop('WOONPLAATS',axis=1)
    df.to_csv('kvg_2017.csv',index=False)

column_picker("Liander_kleinverbruiksgegevens_01012017.csv")



# Liander_kleinverbruiksgegevens_01012009.csv
# Liander_kleinverbruiksgegevens_01012015.csv
# Liander_kleinverbruiksgegevens_01012016.csv