import requests

url = "http://127.0.0.1:5003/prediction"  # Replace with your actual API endpoint

data = {
    "sepal-length": 4.4,
    "sepal-width": 3.2,
    "petal-length": 3.5,
    "petal-width": 3.6
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Failed to get prediction. Status code:", response.status_code)


