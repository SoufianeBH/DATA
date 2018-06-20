import numpy as np
import pandas as pd

from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure, show, output_file

# read data
data = pd.read_csv("lekkerweertje.csv")

dates = [str(x)[:4]+'-'+str(x)[4:6]+'-'+str(x)[6:] for x in data['Date']]
tempmax = [x/10 for x in data['TX']]
tempmin = [x/10 for x in data['TN']]

def avgtempcalculator(datatemp):
    nan = float('nan')
    days = 0
    lastyear = 2009
    totaltemp = 0
    tempmax_avg = []
    for x in range(len(datatemp)):
        totaltemp += datatemp[x]
        days += 1
        if str(lastyear) != str(data["Date"][x])[:4]:
            tempmax_avg.append(totaltemp/days/10)
            totaltemp = 0
            days = 0
            lastyear = int(str(data["Date"][x])[:4])
        else:
            tempmax_avg.append(nan)
    return tempmax_avg

temp = np.array(tempmax)
temp_date = np.array(dates, dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
temp_avg = np.convolve(temp, window, 'same')

p2 = figure(x_axis_type="datetime", title="Maximum temperature")
p2.grid.grid_line_alpha = 0
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Temperature'
p2.ygrid.band_fill_color = "olive"
p2.ygrid.band_fill_alpha = 0.1

p2.circle(temp_date, temp, size=4, legend='close',
          color='darkgrey', alpha=0.2)

p2.line(temp_date, temp_avg, legend='avg', color='navy')
p2.circle(temp_date, avgtempcalculator(data["TX"]), size=10, legend='avg year', color='green', alpha=0.3)

p2.legend.location = "top_left"
tab2 = Panel(child=p2, title="Maximum temperatures")

temp = np.array(tempmin)
temp_date = np.array(dates, dtype=np.datetime64)

temp_avg = np.convolve(temp, window, 'same')

p1 = figure(x_axis_type="datetime", title="Minimum Temperature")
p1.grid.grid_line_alpha = 0
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Temperature'
p1.ygrid.band_fill_color = "olive"
p1.ygrid.band_fill_alpha = 0.1

p1.circle(temp_date, temp, size=4, legend='close',
          color='darkgrey', alpha=0.2)

p1.line(temp_date, temp_avg, legend='avg', color='navy')
p1.circle(temp_date, avgtempcalculator(data["TN"]), size=10, legend='avg year', color='green', alpha=0.3)
p1.legend.location = "top_left"
tab1 = Panel(child=p1, title="Minimum temperatures")

tabs = Tabs(tabs=[ tab1, tab2 ])

output_file("stocks.html", title="stocks.py example")

show(tabs)
