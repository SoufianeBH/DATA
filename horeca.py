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

df.to_csv("horeca.csv",index=False)

data = pd.read_csv("horeca.csv")

fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(data["long"], data["lat"], 'k.', markersize=0.7)

x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
img = plt.imread("kaart.png")
ax.imshow(img, extent = [x0, x1, y0, y1], aspect = "auto", zorder = 0)

plt.savefig("horeca.png")
