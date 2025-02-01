from flask import Flask, request, jsonify
import pickle
import numpy
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Initialise the Flask app
app = Flask(__name__)

# # Load the pre-trained model
# with open("./model/iris_classifier.pkl", "rb") as f:
#     clf = pickle.load(f)

@app.route("/get_status", methods=["GET"])
def get_status():
    return {"training": 70, "testing": 30}

@app.route("/prediction", methods=["POST"]) 
def prediction(): 
    payload = request.json 
    X_unknown = [payload["sepal-length"],payload["sepal-width"],payload["petal-length"],payload["petal-width"]] 
    X_unknown = numpy.array(X_unknown).reshape(1,-1)
    
    with open("./model/iris_classifier.pkl", "rb") as f:
        clf = pickle.load(f)
        prediction = clf.predict(X_unknown) 
        return jsonify({"predicted_value":prediction[0]})
    
    return {"predicted_value": "unknown"}

@app.route("/training", methods=["GET"])
def training():
    # Load the dataset
    df = pd.read_csv("./data/Iris.csv")

    # Define features and target variable
    X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    Y = df['Species']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, shuffle=True)

    # Initialize and train the classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Test the classifier on the testing dataset
    y_pred = clf.predict(X_test)

    # Save the trained model to a file
    with open("./model/iris_classifier.pkl", "wb") as f:
        pickle.dump(clf, f)
    return {"training": 70, "testing": 30, "accuracy": accuracy_score(y_test, y_pred) * 100}

if __name__ == "__main__":
    app.run(port=5000)