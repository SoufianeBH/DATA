import numpy as np
import pandas as pd
import random

from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure, show, output_file

data = pd.read_csv('horecacoor.csv')

lat = [data['lat'][x]*10000 for x in range(len(data['lat']))]
long = [data['long'][x]*10000 for x in range(len(data['long']))]

# color generator
colors = []
for x in range(len(data['long'])):
    if data['long'][x]-4 >= 0.9:
        longcol = (data['long'][x]-4.9)*1500+2
    else:
        longcol = (data['long'][x]-4.8)*500+2
    latcol = (data['lat'][x]-52.3)*100*30+2
    colors.append("#%02x%02x%02x" % (int(max(min(latcol, 255), 160)), 0, int(longcol)))

# colors = [
#     "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
# ]
# for f in range(len(column)):
#     colors.append("#%02x%02x%02x" % (int(f/30), 85, 10))

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

# design the plot with a map
p = figure(tools=TOOLS)
p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

# make scatter plot
radii = [5+2*random.random() for x in range(len(data['lat']))]
x = long
y = lat
p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.65,
          line_color=None)

# output the file
output_file("Horecaoverzicht.html", title="color_scatter.py example")

show(p)  # open a browser
