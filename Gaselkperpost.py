import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file

data = pd.read_csv('clean_data\kvg_2009.csv')

lastpost = 1011
postcheck = 0
elklijst = []
gaslijst = []
count = 0
elk = 0
gas = 0

for x in range(len(data['POSTCODE_TOT'])):
    if lastpost == data['POSTCODE_TOT'][x][:4]:
        if (data['PRODUCTSOORT'][x] == 'ELK') & count == 0:
            elk += data['SJV'][x]
            count = 1
        if count == 1 & (data['PRODUCTSOORT'][x] == 'GAS'):
            gas += data['SJV'][x]
            count = 0
        if count == 1 & (data['PRODUCTSOORT'][x] == 'ELK'):
            elk += data['SJV'][x]
            count = 0
    else:
        elklijst.append(elk)
        gaslijst.append(gas)
        elk, gas = 0, 0
    lastpost = data['POSTCODE_TOT'][x][:4]

x = gaslijst
y = elklijst
gemgrote = [(elklijst[i]+gaslijst[i])/100 for i in range(len(gaslijst))]
radii = [10000 for x in range(len(gaslijst))]

colors = []
for f in radii:
    colors.append("#%02x%02x%02x" % (255, 85, 0))

# colors = [
#     "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
# ]
# print(colors)

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS)
# p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.65,
          line_color=None)

output_file("GAS_ELK.html", title="color_scatter.py example")

show(p)  # open a browser
