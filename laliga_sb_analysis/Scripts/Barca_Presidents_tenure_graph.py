#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:03:57 2021

@author: Derrik Hanson
"""

import plotly.express as px
import pandas as pd

player_tenure = [
    {'prez_name': 'Lionel Messi', 'start':'2004-06-01' ,'end':'2021-06-01'},
    {'prez_name': 'Zlatan Ibrahimovic', 'start':'2009-07-27' ,'end':'2010-08-28'},
    {'prez_name': 'Ronaldinho Gaucho', 'start':'2003-07-19' ,'end':'2008-07-19'},
    {'prez_name': 'Luis Suarez', 'start':'2014-07-11' ,'end':'2021-08-31'},
    {'prez_name': 'Antoine Griezmann', 'start':'2019-07-14' ,'end':'2020-09-25'},
    {'prez_name': 'Samuel Eto\'o', 'start': '2004-08-26' ,'end': '2009-07-27'}
    ]


# load DataFrame
df = pd.DataFrame(player_tenure)


# Create Gantt Plot
fig = px.timeline(df, x_start="start", x_end="end", y="prez_name",
                  labels = {
                      'player_name': 'Player Name'}
                  )
fig.update_layout(
    title={
        'text': "Barcelona Player Tenures",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()

fig.write_image("figures/barca_president_tenure.pdf")