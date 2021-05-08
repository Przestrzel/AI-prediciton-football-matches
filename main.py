import pandas as pd
from pandas import DataFrame as df
import math

teams_val_test = pd.read_csv('Teams Values\\valuesSezon2020.csv')
teams_val_test = teams_val_test[['Team','Value [mln]']]
print(teams_val_test)
