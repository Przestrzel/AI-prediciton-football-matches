import pandas as pd
from pandas import DataFrame as df
import math

#teams_val_test = pd.read_csv('Teams Values\\valuesSezon2020.csv')
#teams_val_test = teams_val_test[['Team','Value [mln]']]

seasonsCount = 10

# cutting csv files to keep only needed data
for i in range(seasonsCount):
    
    seasonMatches = pd.read_csv('Raw Results\\resultsSezon20'+str(i+11)+'.csv')

    # we had to split this becouse column names for betting are diffrent from 2019
    if i < 8:
        cutInfo = seasonMatches[['HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A','BbAv>2.5','BbAv<2.5']]
    else:
        cutInfo = seasonMatches[['HomeTeam','AwayTeam','FTHG','FTAG','FTR','B365H','B365D','B365A','Avg>2.5','Avg<2.5']]
    cutInfo.to_csv('Specified Results\\specInfoSezon20'+str(i+11)+'.csv', index=False)

