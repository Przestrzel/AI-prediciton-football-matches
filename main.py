import prepare_data as data
import pandas as pd

# error 1522 line in ConcatenatedFiles
#data.prepare_data()

#data.count_diffrences()
#data.countForm()
#data.mergeAwithD()



dataset = pd.read_csv("ConcatenatedFiles.csv")

attributes = dataset.drop('FTR', axis = 1)
attributes = attributes.drop('HomeTeam', axis = 1)
attributes = attributes.drop('AwayTeam', axis = 1)
attributes = attributes.drop('HT Form', axis = 1)
attributes = attributes.drop('AT Form', axis = 1)
attributes = attributes.drop('Season', axis = 1)
labels = dataset["FTR"]

#splitting data 60:20:20, train:validate:test
from sklearn.model_selection import train_test_split as split

attributes_train, attributes_test, labels_train, labels_test = split(attributes, labels, test_size = 0.2)

attributes_train, attributes_validate, labels_train, labels_validate = split(attributes_train, labels_train, test_size = 0.25)


#making classifier
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion="entropy", ccp_alpha=0.01)

#testing prunning alpha
from prunning import find_ccp_alpha
path = classifier.cost_complexity_pruning_path(attributes_train, labels_train)
alphas = path['ccp_alphas']

#find_ccp_alpha(alphas, attributes_train, labels_train, attributes_validate, labels_validate)

classifier = classifier.fit(attributes_train, labels_train)

labels_prediction = classifier.predict(attributes_test)

#Raport
from sklearn.metrics import classification_report
print(classification_report(labels_test, labels_prediction))

#only to see what was wrong
labels_test.to_csv('picked matches.csv')
res = pd.read_csv('picked matches.csv')
res['prediction'] = ''
res['prediction'] = labels_prediction
to_drop = []
for ind in res.index:
    if res['FTR'][ind] == res['prediction'][ind]:
        to_drop.append(ind)
res = res.drop(res.index[to_drop])
res.to_csv('picked matches.csv')

#Making visual tree
#import matplotlib.pyplot as plt
#from sklearn import tree
#tree.plot_tree(classifier.fit(attributes_train, labels_train))
#plt.savefig("tree.png")