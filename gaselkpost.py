import numpy as np
import pandas as pd

from bokeh.plotting import figure, show, output_file

data = pd.read_csv('clean_data\kvg_2009.csv')


gaslijst = []
elklijst = []
elk = 0
gas = 0
lastpost = '1011A'
lastpostbig = 1011
colors = []
counter = 0
color = 0
for x in range(len(data['POSTCODE_TOT'])):
    if data['POSTCODE_TOT'][x][:4] != lastpostbig:
        counter += 1
        color = "#%02x%02x%02x" % (int(counter*2), int(counter), int(counter*2))
        print(color)
    if data['POSTCODE_TOT'][x][:5] == lastpost:
        if data['PRODUCTSOORT'][x] == "ELK":
            elk += data['SJV'][x]
        else:
            gas += data['SJV'][x]
    else:
        gaslijst.append(gas)
        elklijst.append(elk)
        colors.append(color)
        if data['PRODUCTSOORT'][x] == "ELK":
            elk = data['SJV'][x]
        else:
            gas = data['SJV'][x]
    lastpost = data['POSTCODE_TOT'][x][:5]
    lastpostbig = data['POSTCODE_TOT'][x][:4]

# hier moet je lijsten ingooien
x = gaslijst
y = elklijst
print(len(x))
print(len(y))
radii = [10000 for x in range(len(y))]

# ook een lijst
# colors = []
# for f in radii:
#     colors.append("#%02x%02x%02x" % (255, 85, 0))

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(tools=TOOLS)
# voor een fotootje
# p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

print(colors)

p.scatter(x, y, radius=radii,
          fill_color=colors, fill_alpha=0.95,
          line_color=None)

output_file("GAS_ELK.html", title="color_scatter.py example")

show(p)  # open a browser
