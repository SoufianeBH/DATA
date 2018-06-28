import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.layouts import row
from bokeh.palettes import Viridis3
from bokeh.models import CheckboxGroup, CustomJS

data = pd.read_csv("GAS_ELK\ELK_2016.csv", decimal=',')

post = pd.read_csv("4pp.csv")

hor = pd.read_csv('horecacoor.csv')


xhor = [float(max(min(x*10000, 50130), 47500)) for x in hor['long']]
yhor = [float(max(min(y*10000, 524200), 522930)) for y in hor['lat']]
radiihor = [5+np.random.random()*2 for x in range(len(hor['long']))]

colorshor = []
for f in range(len(hor['long'])):
    if (hor['long'][f]-4) >= 0.9:
        longcol = (hor['long'][f]-4.9)*1700
    else:
        longcol = (hor['long'][f]-4.8)*700
    latcol = (hor['lat'][f]-52.3)*3200
    colorshor.append("#%02x%02x%02x" % (int(max(min(latcol, 255), 190)), 0, int(longcol)))

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
        coorlistx.append(post["longitude"][y]*10000)
        coorlisty.append(post["latitude"][y]*10000)
        postcodelist.append(post["postcode"][y])

listcounter = 0
for i in range(len(data["POSTCODE_TOT"])):
    if int(data["POSTCODE_TOT"][i][:4]) in ll:
        avg += int(data["SJV"][i]) * int(data["Aantal Aansluitingen"][i]) * (float(data['%Fysieke status'][i])/100)
        counter += 1
    if lastpost != int(data["POSTCODE_TOT"][i][:4]):
        if lastpost in ll:
            ll.remove(lastpost)
        if avg != 0:
            avgpost.append(int(avg/550000))
            avg, counter = 0,0
    lastpost = int(data["POSTCODE_TOT"][i][:4])

xcoor = coorlistx[:-1]
ycoor = coorlisty[:-1]

x = xcoor
y = ycoor
radii = avgpost

colors = []
for f in avgpost:
    colors.append("#%02x%02x%02x" % (int(max(min(f, 255), 65)), int(max(min(150-f, 255), 0)), int(max(min(f*4, 255), 65))))

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS, plot_width=800, plot_height=580, title = 'ELEKTRICITEIT relatief aan horeca')
p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

p.scatter(xhor, yhor, radius=radiihor,
          fill_color=colorshor, fill_alpha=0.8,
          line_color=None)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.5,
          line_color=None)

p2 = figure(tools=TOOLS, plot_width=800, plot_height=580, title = 'ELEKTRICITEIT relatief aan horeca')
p2.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)
p2.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.5,
          line_color=None)

tab1 = Panel(child=p, title='Met horeca')
tab2 = Panel(child=p2, title='Zonder horeca')

tabs = Tabs(tabs=[tab1,tab2])

output_file("MAP_ELK_hor.html", title="color_scatter.py example")

show(tabs)  # open a browser
