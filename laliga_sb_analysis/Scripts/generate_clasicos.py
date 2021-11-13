#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:31:08 2021

@author: Spade5
"""
import pandas as pd
import numpy as np 


# --------
mfilep = "laliga_sb_analysis/laliga_data/matches_laliga.csv"
with open(mfilep, 'r') as f:
    liga_matches = pd.read_csv(f)
    


clasico_mask1 = liga_matches['home_team'] == 'Real Madrid'
clasico_mask2 = liga_matches['away_team'] == 'Real Madrid'

clasicos_1 = liga_matches[clasico_mask1]
clasicos_2 = liga_matches[clasico_mask2]

clasicos_all =  pd.concat([clasicos_1, clasicos_2]).drop(['barca_played'], axis=1)
clasicos_all['match_date'] = pd.to_datetime(clasicos_all['match_date'], format = '%Y-%m-%d')
clasicos_all.sort_values(by=['match_date'], ascending=False, inplace=True)
clasicos_all.reset_index(inplace=True)

clasicos_all.to_csv("laliga_sb_analysis/laliga_data/clasico_matches.csv")

