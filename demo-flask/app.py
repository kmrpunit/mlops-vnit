import json
from flask import Flask, request, jsonify, render_template
import pickle
import numpy
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Initialise the Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/get_status", methods=["GET"])
def get_status():
    return {"training": 70, "testing": 30}

@app.route("/prediction", methods=["POST"]) 
def prediction(): 
    payload_json = request.get_json()
    print(payload_json)
    payload = json.loads(payload_json)
    X_unknown = [payload["sepal-length"],payload["sepal-width"],payload["petal-length"],payload["petal-width"]] 
    X_unknown = numpy.array(X_unknown).reshape(1,-1)
    
    with open("./model/iris_classifier.pkl", "rb") as f:
        clf = pickle.load(f)
        prediction = clf.predict(X_unknown) 
        return jsonify({"predicted_value":prediction[0]})
    
    return {"predicted_value": "unknown"}

@app.route("/training", methods=["GET"])
def training():
    try:
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
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)