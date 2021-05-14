import prepare_data as data
import pandas as pd


#data.prepare_data()
#data.count_diffrences() 

dataset = pd.read_csv("ConcatenatedFiles.csv")

attributes = dataset.drop('FTR', axis = 1)
labels = dataset["FTR"]

