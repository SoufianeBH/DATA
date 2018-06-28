import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.layouts import row
from bokeh.palettes import Viridis3
from bokeh.models import CheckboxGroup, CustomJS
import folium
from folium.plugins import MarkerCluster

m = folium.Map(location=[52.36424,4.883358],
                    zoom_start = 12, tiles="CartoDB Positron",
                            control_scale=True)

data09 = pd.read_csv("GAS_ELK\ELK_2009.csv", decimal=',')
data10 = pd.read_csv("GAS_ELK\ELK_2010.csv", decimal=',')
data11 = pd.read_csv("GAS_ELK\ELK_2011.csv", decimal=',')
data12 = pd.read_csv("GAS_ELK\ELK_2012.csv", decimal=',')
data13 = pd.read_csv("GAS_ELK\ELK_2013.csv", decimal=',')
data14 = pd.read_csv("GAS_ELK\ELK_2014.csv", decimal=',')
data15 = pd.read_csv("GAS_ELK\ELK_2015.csv", decimal=',')
data = pd.read_csv("GAS_ELK\ELK_2016.csv", decimal=',')

post = pd.read_csv("4pp.csv")

avg = 0
counter = 0
lastpost = 1011

values = []
xcoor = []
ycoor = []

coorlistx = []
coorlisty = []
postcodelist = []
ll = []
avgpost = []

for j in data["POSTCODE_TOT"]:
    if int(j[:4]) not in ll:
        ll.append(int(j[:4]))

for y in range(len(post["postcode"])):
    if int(post["postcode"][y]) in ll:
        coorlistx.append(post["latitude"][y])
        coorlisty.append(post["longitude"][y])
        postcodelist.append(str(post["postcode"][y]))

listcounter = 0
for i in range(len(data["POSTCODE_TOT"])):
    if int(data["POSTCODE_TOT"][i][:4]) in ll:
        avg += int(data["SJV"][i]) * int(data["Aantal Aansluitingen"][i]) * (float(data['%Fysieke status'][i])/100)
    if lastpost != int(data["POSTCODE_TOT"][i][:4]):
        if lastpost in ll:
            ll.remove(lastpost)
        if avg != 0:
            postcodelist[counter] = str('Postcode: '+str(postcodelist[counter])+' | Stroomverbruik: '+str(int(avg)))
            counter += 1
            avgpost.append(int(avg/550000))
            avg = 0
    lastpost = int(data["POSTCODE_TOT"][i][:4])

xcoor = coorlistx[:-1]
ycoor = coorlisty[:-1]

marker_cluster = MarkerCluster().add_to(m)

for i in range(len(xcoor)):
    lat = xcoor[i]
    lon = ycoor[i]

    address = postcodelist[i]

    folium.RegularPolygonMarker(location=(lat, lon), popup=address, fill_color='#2b8cbe', number_of_sides=20, radius=6).add_to(marker_cluster)

m.save('amsterdammap.html')
m
