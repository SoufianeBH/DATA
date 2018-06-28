
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file

elk = pd.read_csv("clean_data/elk_2009.csv")
weer = pd.read_csv("weer2009.csv")

p1 = figure(title="Totale Stroomverbruik en temperatuur in 2009")
p1.grid.grid_line_alpha = 0
p1.xaxis.axis_label = 'Datum'
p1.yaxis.axis_label = 'Stroomverbruik'
p1.ygrid.band_fill_color = "olive"
p1.ygrid.band_fill_alpha = 0.1

nan = float('nan')
totaal = []
dag = []
temp = []
for i in range(len(elk['Totaal'])):
    if i >= 1:
        totaal.append(elk['Totaal'][i])
        dag.append(elk['Dag'][i])
        temp.append(weer['TX'][i]*500)
    else:
        temp.append(nan)
        totaal.append(nan)
        dag.append(nan)

dag[-1] = nan
totaal[-1] = nan
temp[-1] = nan

window_size = 20
window = np.ones(window_size)/float(window_size)
elek = np.convolve(totaal, window, 'same')
temp = np.convolve(temp, np.ones(30)/float(30), 'same')

p1.line(dag, elek, legend='stroom', color='navy')
p1.line(dag, temp, legend='temperatuur', color='green')

output_file("stroom2009.html", title="stroom.py example")
show(p1)
