import pandas as pd
from pandas import DataFrame as df
import glob

def prepare_data():  
    seasons_counter = 10

    # cutting csv files to keep only needed data
    for i in range(seasons_counter):
        season_year = i + 11 + 2000
        season_string = str(season_year)

        season_matches = pd.read_csv('Raw Results\\resultsSezon'+season_string+'.csv')

        # we had to split this because column names for betting are diffrent from 2019
        cutInfo = season_matches[['HomeTeam','AwayTeam','FTR','B365H','BbAv>2.5']]
        cutInfo['Season'] = season_string
        
        cutInfo.to_csv('Specified Results\\specInfoSezon'+ season_string +'.csv', index=False)

    # splitted results to one file
    path = r'C:\Users\marek\OneDrive\Dokumenty\GitHub\AI-prediciton-football-matches\Specified Results' #your path to project

    all_files = glob.glob(path + "\*.csv") 
    list = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        list.append(df)

    frame = pd.concat(list, axis = 0, ignore_index=True)

    frame.to_csv("ConcatenatedFiles.csv", index=False)

    # count diffrents in opponents values
def count_diffrences():
    df_matches = pd.read_csv('ConcatenatedFiles.csv')
    df_matches['HT VAL/AT VAL'] = ""
    for ind in df_matches.index:
        
        season = df_matches['Season'][ind]
        season_string = str(season)
        home_team = df_matches['HomeTeam'][ind]
        away_team = df_matches['AwayTeam'][ind]

        # finding home and away team values in csv with club values
        df_val = pd.read_csv('Teams Values\\valuesSezon'+season_string+'.csv')

        h_val = df_val.loc[df_val['Team'] == home_team]
        a_val = df_val.loc[df_val['Team'] == away_team]

        h_val = h_val['Value [mln]']
        a_val = a_val['Value [mln]']

        #df_matches['Diffrence'][ind] = float(h_val) - float(a_val)
        df_matches['HT VAL/AT VAL'][ind] = float(h_val) / float(a_val)

    df_matches.to_csv("ConcatenatedFiles.csv", index=False)    
        

