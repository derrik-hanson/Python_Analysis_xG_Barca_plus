#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:39:17 2021

@author: Derrik Hanson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:03:57 2021

@author: Derrik Hanson
"""

import plotly.express as px
import pandas as pd

manager_tenures = [
    {'manager_name': 'Frank Rijkaard', 'start':'2003-06' ,'end':'2008-06'},
    {'manager_name': 'Pep Guardiola', 'start':'2008-06' ,'end':'2012-06'},
    {'manager_name': 'Tito Vilanova', 'start':'2012-07' ,'end':'2013-01'},
    {'manager_name': 'Jordi Roura', 'start':'2013-01' ,'end':'2013-03'},
    {'manager_name': 'Tito Vilanova', 'start':'2013-03' ,'end':'2013-07'},
    {'manager_name': 'Gerard Martino', 'start':'2013-07' ,'end':'2014-05'},
    {'manager_name': 'Luis Enrique', 'start':'2014-05' ,'end':'2017-05'},
    {'manager_name': 'Ernesto Valverde', 'start':'2017-05' ,'end':'2020-01'},
    {'manager_name': 'Quique Setien', 'start':'2020-01' ,'end':'2020-08'},
    {'manager_name': 'Ronald Koeman', 'start':'2020-08' ,'end':'2021-10'},
    ]


# load DataFrame
df = pd.DataFrame(manager_tenures)


# Create Gantt Plot
fig = px.timeline(df, x_start="start", x_end="end", y="manager_name",
                  labels = {
                      'manager_name': 'Manager Name'}
                  )
fig.update_layout(
    title={
        'text': "Barcelona Manager Tenures",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.update_yaxes(autorange="reversed") # otherwise tasks are slisted from the bottom up
fig.show()

fig.write_image("figures/barca_manager_tenure.pdf")