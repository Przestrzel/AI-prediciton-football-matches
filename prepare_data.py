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
        cutInfo = season_matches[['HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A','BbAv>2.5','BbAv<2.5']]
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


