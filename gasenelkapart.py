import pandas as pd

data = pd.read_csv("clean_data\kvg_2016.csv")

data[data.PRODUCTSOORT == "ELK"].to_csv("GAS_ELK\ELK_2016.csv", index=False)
