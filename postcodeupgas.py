import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.models.widgets import Panel, Tabs

data09 = pd.read_csv("GAS_ELK\GAS_2009.csv")
data10 = pd.read_csv("GAS_ELK\GAS_2010.csv")
data11 = pd.read_csv("GAS_ELK\GAS_2011.csv")
data12 = pd.read_csv("GAS_ELK\GAS_2012.csv")
data13 = pd.read_csv("GAS_ELK\GAS_2013.csv")
data14 = pd.read_csv("GAS_ELK\GAS_2014.csv")
data15 = pd.read_csv("GAS_ELK\GAS_2015.csv")
data16 = pd.read_csv("GAS_ELK\GAS_2016.csv")

post = pd.read_csv("4pp.csv")

def plotmaker(data):
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
            counter += 1
        if lastpost != int(data["POSTCODE_TOT"][i][:4]):
            if lastpost in ll:
                ll.remove(lastpost)
            if avg != 0:
                avgpost.append(int(avg/200000))
                avg, counter = 0,0
        lastpost = int(data["POSTCODE_TOT"][i][:4])

    xcoor = coorlistx[:-1]
    ycoor = coorlisty[:-1]

    x = xcoor
    y = ycoor
    radii = avgpost

    colors = []
    for f in avgpost:
        colors.append("#%02x%02x%02x" % (int(max(min(f*3, 255), 65)), int(max(min(255-f*2.5, 255), 0)), 0))


    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

    p = figure(tools=TOOLS, plot_width=800, plot_height=580, title='GAS door de jaren')
    p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

    p.scatter(x, y, radius=radii,
              fill_color=colors, fill_alpha=0.8,
              line_color=None)

    global year
    year = str(int(year)+1)

    tab = Panel(child=p, title=year)

    return tab

year = '2008'

tabs = Tabs(tabs=[plotmaker(data09),plotmaker(data10),plotmaker(data11),plotmaker(data12),plotmaker(data13),plotmaker(data14),plotmaker(data15),plotmaker(data16)])

output_file("MAPup_GAS.html", title="color_scatter.py example")

show(tabs)  # open a browser
