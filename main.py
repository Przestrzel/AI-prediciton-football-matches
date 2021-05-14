import prepare_data as data
import pandas as pd
#data.prepare_data()
#data.count_diffrences() 

dataset = pd.read_csv("ConcatenatedFiles.csv")

attributes = dataset.drop('FTR', axis = 1)
attributes = attributes.drop('HomeTeam', axis = 1)
attributes = attributes.drop('AwayTeam', axis = 1)
labels = dataset["FTR"]

#splitting data 60:20:20, train:validate:test
from sklearn.model_selection import train_test_split as split

attributes_train, attributes_test, labels_train, labels_test = split(attributes, labels, test_size = 0.2)

attributes_train, attributes_validate, labels_train, labels_validate = split(attributes_train, labels_train, test_size = 0.25)

#making classifier
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion="entropy", ccp_alpha=0.0002)

classifier = classifier.fit(attributes_train, labels_train)

labels_prediction = classifier.predict(attributes_test)

#Raport
from sklearn.metrics import classification_report
print(classification_report(labels_test, labels_prediction))

#Making visual tree
#import matplotlib.pyplot as plt
#from sklearn import tree
#tree.plot_tree(classifier.fit(attributes_train, labels_train))
#plt.savefig("tree.png")