import pandas as pd
import matplotlib.pyplot as plt

# read data
cols = [*range(3,7),8,*range(10,13),16,17]
data = pd.read_csv('2016data.csv', engine="python", sep="\t", usecols=cols)

condition = (data["WOONPLAATS"] == "AMSTERDAM")|(data["WOONPLAATS"] == "AMSTERDAM ZUIDOOST")|(data["WOONPLAATS"] == "AMSTERDAM ZUID00ST")|(data["WOONPLAATS"] == "AMSTERDAM DUIVENDRECHT")
data = data.loc[condition]




print(data["PRODUCTSOORT"])
