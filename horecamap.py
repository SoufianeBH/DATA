import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file

data = pd.read_csv('horecacoor.csv')


x = [x*10000 for x in data['long']]
y = [y*10000 for y in data['lat']]
radii = [5+np.random.random()*2 for x in range(len(data['long']))]

colors = []
for f in range(len(data['long'])):
    if (data['long'][f]-4) >= 0.9:
        longcol = (data['long'][f]-4.9)*1700
    else:
        longcol = (data['long'][f]-4.8)*700
    latcol = (data['lat'][f]-52.3)*3200
    print(longcol)
    colors.append("#%02x%02x%02x" % (int(max(min(latcol, 255), 190)), 0, int(longcol)))

# colors = [
#     "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
# ]
# print(colors)

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS)
p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.65,
          line_color=None)

output_file("horecamap.html", title="color_scatter.py example")

show(p)  # open a browser
