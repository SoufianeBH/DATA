import pandas as pd

def call_file():
    year = int(input("year: "))
    df = pd.read_csv("test_kvg_%i.csv"% year , sep=None, engine="python" )
    # print(df.head())
    return df


call_file()