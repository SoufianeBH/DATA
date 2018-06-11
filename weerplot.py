import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read data
data = pd.read_csv("lekkerweertje.csv")

# plot long and lat data
date = []
tempx = []
tempn = []
tempg = []
counter = 0
counterg = 0
avgx = 0
avgn = 0
avgg = 0
lastdeg = data["TG"][0]

for i in range(len(data["Date"])):
    counter += 1
    counterg += 1
    avgx += data["TX"][i]
    avgn += data["TN"][i]
    avgg += data["TG"][i]
    if counterg == 363:
        lastdeg = avgg/3630
        avgg = 0
        counterg = 0
    if counter == 25:
        tempg.append(lastdeg)
        tempx.append(avgx/250)
        tempn.append(avgn/250)
        date.append(str(data["Date"][i])[:4]+"/"+str(data["Date"][i])[4:6]+"/"+str(data["Date"][i])[6:])
        counter = 0
        avgx, avgn = 0, 0

plt.locator_params(nbins=25)
plt.figure(figsize=(25,6))
plt.plot(date, tempx)
plt.plot(date, tempn)
plt.plot(date, tempg)


# save plot
plt.savefig("temp.png")

plt.show()
