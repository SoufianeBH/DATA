# Import the necessary modules
from bokeh.layouts import row, widgetbox
from bokeh.models import Slider

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # set the `yr` name to `slider.value` and `source.data = new_data`
    yr = slider.value
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    source.data = new_data


# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)

show(layout)

# import numpy as np
# import pandas as pd
#
# from bokeh.plotting import figure, show, output_file
#
# data = pd.read_csv("GAS_ELK\GAS_2016.csv")
# post = pd.read_csv("4pp.csv")
#
# avg = 0
# counter = 0
# lastpost = 1011
#
# values = []
# xcoor = []
# ycoor = []
#
# coorlistx = []
# coorlisty = []
# postcodelist = []
# ll = []
# avgpost = []
#
# for j in data["POSTCODE_TOT"]:
#     if int(j[:4]) not in ll:
#         ll.append(int(j[:4]))
#
# for y in range(len(post["postcode"])):
#     if int(post["postcode"][y]) in ll:
#         coorlistx.append(post["longitude"][y]*10000)
#         coorlisty.append(post["latitude"][y]*10000)
#         postcodelist.append(post["postcode"][y])
#
# print(len(postcodelist))
# print(len(coorlistx))
# print(len(coorlisty))
# print(coorlistx)
# print(coorlisty)
#
#
# listcounter = 0
# for i in range(len(data["POSTCODE_TOT"])):
#     if int(data["POSTCODE_TOT"][i][:4]) in ll:
#         avg += int(data["SJV"][i]) * int(data["Aantal Aansluitingen"][i])
#         counter += int(data["Aantal Aansluitingen"][i])
#     if lastpost != int(data["POSTCODE_TOT"][i][:4]):
#         if lastpost in ll:
#             ll.remove(lastpost)
#         if avg != 0:
#             avgpost.append(int((avg/counter)/55))
#             avg, counter = 0,0
#     lastpost = int(data["POSTCODE_TOT"][i][:4])
#
# xcoor = coorlistx[:-1]
# ycoor = coorlisty[:-1]
# print(len(avgpost))
#
#
# # for x in range(len(post["postcode"])):
# #     if int(post["postcode"][x]) >= 1011 and int(post["postcode"][x]) <= 1109:
# #         xcoor.append(int(post["latitude"][x]))
# #         ycoor.append(int(post["longitude"][x]))
#
# # for i in range(len(data["SJV"])):
# #     avg += int(data["SJV"][i])
# #     counter += 1
# #     # print(lastpost)
# #     # print(data["POSTCODE_TOT"][i])
# #     if lastpost != int(data["POSTCODE_TOT"][i][:4]):
# #         if int(lastpost) in list(post["postcode"]):
# #             values.append(float(avg/counter))
# #             counter = 0
# #             avg = 0
# #         else:
# #             counter = 0
# #             avg = 0
# #     lastpost = int(data["POSTCODE_TOT"][i][:4])
# #
# #
# x = xcoor
# y = ycoor
# # x = np.random.random(size=N) * 100
# # y = np.random.random(size=N) * 100
# radii = avgpost
# print(max(xcoor))
# print(min(xcoor))
# print(max(ycoor))
# print(min(ycoor))
# colors = []
# for f in avgpost:
#     colors.append("#%02x%02x%02x" % (int(f), 85, 170))
#
# # colors = [
# #     "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
# # ]
# # print(colors)
#
# TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"
#
# p = figure(tools=TOOLS)
# p.image_url(url=['Capture.png'],w=2668,h=1328, x=47494.287, y=524238.336)
#
# p.scatter(x, y, radius=radii,
#           fill_color=colors, fill_alpha=0.65,
#           line_color=None)
#
# output_file("MAP_GAS_2016.html", title="color_scatter.py example")
#
# show(p)  # open a browser
