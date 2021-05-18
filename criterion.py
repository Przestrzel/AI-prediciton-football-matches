import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split as split

# the experiment of which criterion to choose - gini or entropy

def create_graph(attributes, labels):
    acc_entropy_plain, acc_gini_plain, acc_entropy_prunning, acc_gini_prunning = [], [], [], []

    for _ in range(20):
        attr_train, attr_validate, labels_train, labels_validate = split(attributes, labels, test_size = 0.3)
        classifier = DecisionTreeClassifier(criterion="entropy")
        classifier.fit(attr_train, labels_train)
        
        labels_predict_validate = classifier.predict(attr_validate)
        acc_entropy_plain.append(accuracy_score(labels_validate, labels_predict_validate))

    for _ in range(20):
        attr_train, attr_validate, labels_train, labels_validate = split(attributes, labels, test_size = 0.3)
        classifier = DecisionTreeClassifier(criterion="entropy", ccp_alpha=0.01)
        classifier.fit(attr_train, labels_train)
        
        labels_predict_validate = classifier.predict(attr_validate)
        acc_entropy_prunning.append(accuracy_score(labels_validate, labels_predict_validate))

    for _ in range(20):
        attr_train, attr_validate, labels_train, labels_validate = split(attributes, labels, test_size = 0.3)
        classifier = DecisionTreeClassifier(criterion="gini")
        classifier.fit(attr_train, labels_train)
        
        labels_predict_validate = classifier.predict(attr_validate)
        acc_gini_plain.append(accuracy_score(labels_validate, labels_predict_validate))

    for _ in range(20):
        attr_train, attr_validate, labels_train, labels_validate = split(attributes, labels, test_size = 0.3)
        classifier = DecisionTreeClassifier(criterion="gini", ccp_alpha=0.01)
        classifier.fit(attr_train, labels_train)
        
        labels_predict_validate = classifier.predict(attr_validate)
        acc_gini_prunning.append(accuracy_score(labels_validate, labels_predict_validate))

    #creating comparing graph
    df = pd.DataFrame(columns = ["Entropy", "Entropy prunning", "Gini", "Gini prunning"])
    df["Entropy"] = acc_entropy_plain
    df["Entropy prunning"] = acc_entropy_prunning
    df["Gini"] = acc_gini_plain
    df["Gini prunning"] = acc_gini_prunning
    
    print(pd.melt(df))
    sns.boxplot(x="variable", y="value", data=pd.melt(df))   
    plt.savefig("graphs/criterion.png")