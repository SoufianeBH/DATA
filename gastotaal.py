import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file

negen = pd.read_csv("GAS_ELK/GAS_2009.csv")
tien = pd.read_csv("GAS_ELK/GAS_2010.csv")
elf = pd.read_csv("GAS_ELK/GAS_2011.csv")
twaalf = pd.read_csv("GAS_ELK/GAS_2012.csv")
dertien = pd.read_csv("GAS_ELK/GAS_2013.csv")
veertien = pd.read_csv("GAS_ELK/GAS_2014.csv")
vijftien = pd.read_csv("GAS_ELK/GAS_2015.csv")
zestien = pd.read_csv("GAS_ELK/GAS_2016.csv")

perjaar = []
jaartal = ['2009','2010','2011','2012','2013','2014','2015','2016']

def counter(jaren):
    total = 0
    for i in range(len(jaren["SJV"])):
        total += int(jaren["SJV"][i]) * int(jaren["Aantal Aansluitingen"][i])
    return total


perjaar.append(counter(negen))
perjaar.append(counter(tien))
perjaar.append(counter(elf))
perjaar.append(counter(twaalf))
perjaar.append(counter(dertien))
perjaar.append(counter(veertien))
perjaar.append(counter(vijftien))
perjaar.append(counter(zestien))

print(perjaar)

p1 = figure(x_axis_type="datetime", title="Totale Gasverbruik")
p1.grid.grid_line_alpha = 0
p1.xaxis.axis_label = 'Datum'
p1.yaxis.axis_label = 'Gasverbruik'
p1.ygrid.band_fill_color = "olive"
p1.ygrid.band_fill_alpha = 0.1

p1.line(jaartal, perjaar, legend='gas', color='navy')

output_file("gas.html", title="gas.py example")
show(p1)
