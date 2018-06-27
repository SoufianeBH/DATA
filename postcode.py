import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file

data = pd.read_csv("GAS_ELK\ELK_2015.csv")

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
        coorlistx.append(post["longitude"][y]*10000)
        coorlisty.append(post["latitude"][y]*10000)
        postcodelist.append(post["postcode"][y])

listcounter = 0
for i in range(len(data["POSTCODE_TOT"])):
    if int(data["POSTCODE_TOT"][i][:4]) in ll:
        avg += int(data["SJV"][i]) * int(data["Aantal Aansluitingen"][i])
        counter += int(data["Aantal Aansluitingen"][i])
    if lastpost != int(data["POSTCODE_TOT"][i][:4]):
        if lastpost in ll:
            ll.remove(lastpost)
        if avg != 0:
            avgpost.append(int((avg/counter)/55))
            avg, counter = 0,0
    lastpost = int(data["POSTCODE_TOT"][i][:4])

xcoor = coorlistx[:-1]
ycoor = coorlisty[:-1]

x = xcoor
y = ycoor
radii = avgpost

colors = []
for f in avgpost:
    colors.append("#%02x%02x%02x" % (int(max(min(f, 255), 0)), 85, 170))

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS)
p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.65,
          line_color=None)

output_file("MAP_ELK_2015.html", title="color_scatter.py example")

print(avgpost[73])

show(p)  # open a browser
