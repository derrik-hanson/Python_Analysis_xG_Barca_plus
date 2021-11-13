#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:03:57 2021

@author: Derrik Hanson
"""

import plotly.express as px
import pandas as pd

president_tenure = [
    {'prez_name': 'Joan Laporta', 'start':'2003-06-15' ,'end':'2010-07-01'},
    {'prez_name': 'Joan Laporta', 'start':'2021-03-07' ,'end':'2021-11-12'},
    {'prez_name': 'Sandro Rosell', 'start':'2010-07-01' ,'end':'2014-01-23'},
    {'prez_name': 'Josep Bartomeu', 'start':'2014-01-23' ,'end':'2020-10-27'},
    {'prez_name': 'Carles Tusquets', 'start':'2020-10-29' ,'end':'2021-03-07'},
    ]


# load DataFrame
df = pd.DataFrame(president_tenure)


# Create Gantt Plot
fig = px.timeline(df, x_start="start", x_end="end", y="prez_name",
                  labels = {
                      'prez_name': 'President Name'}
                  )
fig.update_layout(
    title={
        'text': "Barcelona President Tenures",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()

fig.write_image("figures/barca_president_tenure.pdf")