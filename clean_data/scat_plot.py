import pandas as pd 
import numpy as np 
from bokeh.plotting import figure, show, output_file

def color_scatter(value,x,y):
    color_code = str("#%02x%02x%02x" % (int(max(min(y[value]/100, 255), 0)), int(max(min(y[value]/10000,255),140)), 0))
    return color_code

    # colors.append("#%02x%02x%02x" % (int(max(min((gaslijst[i]+elklijst[i])/8500, 255), 140)), int(max(min(255-(elklijst[i]/3+gaslijst[i]/5)/8000, 200), 0)), 0))

def scatter_plot(x_as,y_as):
    # hier moet je lijsten ingooien 
    x = x_as
    y = y_as
    radii = [5 for x in range(len(y_as))]

    # ook een lijst
    colors = []
    for i in range(len(x_as)):
        colors.append(color_scatter(i,x,y))
        # colors.append("#%02x%02x%02x" % (int(max(min(y[i]/100, 255), 140)), int(max(min(x[i]/200,255),140)), 0))

    TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

    p = figure(tools=TOOLS)
    # voor een fotootje
    # p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)

    p.scatter(x, y, radius=radii,
            fill_color=colors, fill_alpha=0.65,
            line_color=None)

    output_file("Fys_SJV.html", title="color_scatter.py example")

    show(p)  # open a browser


def listmaker(df):
    fys_st = df['%Fysieke status']
    aantal = df['Aantal Aansluitingen']
    y_as = df['SJV']

    x_as = [int(float(f/100)*a) for f, a in zip(fys_st, aantal)]
    scatter_plot(x_as,y_as)


def call_file():
    year = int(input("year:"))
    df = pd.read_csv("test_kvg_%i.csv"% year , sep=None, engine="python" )
    print(df.head())


# call_file()

df = pd.read_csv("test_kvg_2009.csv", sep=None, engine="python")
listmaker(df)
