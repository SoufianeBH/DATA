import pandas as pd
import re
import matplotlib.pyplot as plt

data = pd.read_csv("testhoreca.csv",usecols=[6])

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

long = []
lat = []
number = ""
spatie = False
for x in data["LOCATIE_WKT"]:
    x = x.replace("POINT (", "").replace(")", " ")
    spatie = False
    for numb in x:
        if numb == " ":
            if spatie == False:
                long.append(float(number))
            if spatie == True:
                lat.append(float(number))
            spatie = True
            number = ""
        if numb != " ":
            number += numb


d = {'long': long, 'lat': lat}
df = pd.DataFrame(data=d)

df.to_csv("horecacoor.csv",index=False)

