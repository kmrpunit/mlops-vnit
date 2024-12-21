from sklearn import datasets
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score from utils import split_data

df = pd.read_csv("./data/Iris.csv")
X_train, X_test, y_train, y_test = split_data(df)

#step-1: initialise the model class
clf = DecisionTreeClassifier(criterion="gini") #gini as criterion

#step-2: train the model on training set
clf.fit(x_train,y_train)

#step-3 evaluate the data on testing set
y_pred = clf.predict(X_test)

print(f"Accuacy of the model is {faccuracy_score(y_test, y_pred) * 180}") #--> this test accuracy