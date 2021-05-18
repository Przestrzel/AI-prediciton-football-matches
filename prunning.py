from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
import numpy as np


# find best ccp_alpha
def find_ccp_alpha(alphas, attributes_train, labels_train, attributes_validate, labels_validate):
    accuracy_train, accuracy_validate = [], []

    for alpha in alphas:
        classifier = DecisionTreeClassifier(criterion="entropy", ccp_alpha = alpha)

        classifier.fit(attributes_train, labels_train)
        labels_predict_train = classifier.predict(attributes_train)
        labels_predict_validate = classifier.predict(attributes_validate)

        accuracy_train.append(accuracy_score(labels_train, labels_predict_train))
        accuracy_validate.append(accuracy_score(labels_validate, labels_predict_validate))
    
    sns.set()
    plt.figure(figsize=(20, 10))
    sns.lineplot(y=accuracy_train, x=alphas, label="Train accuracy")
    sns.lineplot(y=accuracy_validate, x=alphas, label="Validate accuracy")
    plt.xticks(ticks=np.arange(0.00, 0.10, 0.01))
    plt.savefig("graphs/prunning.png")
