#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:23:41 2021

@author: Derrik Hanson
"""

import matplotlib.pyplot as plt
import numpy as np
import json
from FCPython import createPitch

def plot_shots_home_away(match_id_required, home_team_required, away_team_required):
    # Size of the pitch in yards 
    pitchLengthX=120
    pitchWidthY=80

    # ----------------
    #Load in all match events 
    file_name=str(match_id_required)+'.json'
    
    with open('statsbomby/data/events/'+file_name) as data_file:
        data = json.load(data_file)
    
    
    
    # ----------------
    # get the nested structure into a dataframe 
    # store the dataframe in a dictionary with the match id as key (remove '.json' from string)
    from pandas.io.json import json_normalize
    df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    
    #A dataframe of shots
    shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
    
    # ----------------    
    #Draw the pitch
    (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
    
    #Plot the shots
    for i,shot in shots.iterrows():
        x=shot['location'][0]
        y=shot['location'][1]
        
        goal=shot['shot_outcome_name']=='Goal'
        team_name=shot['team_name']
        
        circleSize=2
        #circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12
    
        if (team_name==home_team_required):
            if goal:
                shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
                plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
            else:
                shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="grey")     
                shotCircle.set_alpha(.2)
        elif (team_name==away_team_required):
            if goal:
                shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue") 
                plt.text((pitchLengthX-x+1),y+1,shot['player_name']) 
            else:
                shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="grey")      
                shotCircle.set_alpha(.2)
        else:
            print('did you enter both team names correctly?')
        ax.add_patch(shotCircle)
        
        
    plt.text(7,75,away_team_required + ' shots') 
    plt.text(95,75,home_team_required + ' shots') 
         
    fig.set_size_inches(10, 7)
    # fig.savefig('Output/shots.pdf', dpi=100) 
    plt.show()


def plot_shots_player(events_df_in, player_name,in_title_text = ''):
    # Size of the pitch in yards 
    pitchLengthX=120
    pitchWidthY=80
    # ----------------

    #A dataframe of shots
    shot_mask = events_df_in['type_name'] == 'Shot'
    shots = events_df_in.loc[shot_mask]#.set_index('id')
    player_mask = shots['player_name'] == player_name
    shots = shots[player_mask]#.set_index('id')
    
    # ----------------    
    #Draw the pitch
    (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
    
    #Plot the shots
    for i,shot in shots.iterrows():
        x=shot['location'][0]
        y=shot['location'][1]
        
        goal=shot['shot_outcome_name']=='Goal'

        circleSize=2
        #circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12
    
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            # plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
        else:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="grey")     
            shotCircle.set_alpha(.2)

        ax.add_patch(shotCircle)
        
        
    # plt.text(7,75,away_team_required + ' shots') 
    plt.text(95,75,'shots:' + player_name) 
    plt.text(75, 75, in_title_text)
         
    fig.set_size_inches(10, 7)
    fig.savefig(f"Output/shots/{player_name}_{in_title_text}.pdf", dpi=100) 
    plt.show()

def plot_goals_player(events_df_in, player_name,in_title_text = ''):
    # Size of the pitch in yards 
    pitchLengthX=120
    pitchWidthY=80
    # ----------------

    #A dataframe of shots
    shot_mask = events_df_in['type_name'] == 'Shot'
    shots = events_df_in.loc[shot_mask]#.set_index('id')
    player_mask = shots['player_name'] == player_name
    shots = shots[player_mask]#.set_index('id')
    
    # ----------------    
    #Draw the pitch
    (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
    
    #Plot the shots
    for i,shot in shots.iterrows():
        x=shot['location'][0]
        y=shot['location'][1]
        
        goal=shot['shot_outcome_name']=='Goal'

        circleSize=2
        circleSize=np.sqrt(shot['shot_statsbomb_xg'])*5
    
        if goal:
            shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="red")
            # plt.text((x+1),pitchWidthY-y+1,shot['player_name']) 
            shotCircle.set_alpha(0.4)
            ax.add_patch(shotCircle)
        # else:
        #     shotCircle=plt.Circle((x,pitchWidthY-y),circleSize,color="grey")     
        #     shotCircle.set_alpha(.2)

        
        
        
    # plt.text(7,75,away_team_required + ' shots') 
    plt.text(75,75,'goals :' + in_title_text) 
    plt.text(75, 65, player_name)
    plt.text(75, 70, 'radius ~ xG')
         
    fig.set_size_inches(10, 7)
    fig.savefig(f"Output/goals/{player_name}_{in_title_text}.pdf", dpi=100) 
    plt.show()


# -------------------
# test runs
plot_shots_home_away(303430, 'Barcelona', 'Villarreal')


# -------------------
# test runs
plot_shots_home_away(303430, 'Barcelona', 'Villarreal')

