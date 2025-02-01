# Demo Flask Application

This is a simple Flask application that can be run using Docker.

## Prerequisites

- Docker installed on your machine

## Running the Application

1. Clone the repository:

    ```sh
    git clone https://github.com/your-repo/demo-flask.git
    cd demo-flask
    ```

2. Build the Docker image:

    ```sh
    docker build -t demo-flask .
    ```

3. Run the Docker container:

    ```sh
    docker run -p 5000:5000 demo-flask
    ```

4. Open your web browser and go to `http://localhost:5000` to see the application running.

## Using a Different Port

If you want to run the application on a different port, you can specify the desired port in the `docker run` command. For example, to run the application on port 8080:

    ```sh
    docker run -p 8080:5000 demo-flask
    ```

Then, open your web browser and go to `http://localhost:8080` to see the application running.

## Dockerfile

Make sure you have a `Dockerfile` in the root of your project with the following content:

    ```Dockerfile
    # Use the official Python image as a base image
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the requirements file into the container
    COPY requirements.txt .

    # Install the dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the rest of the application files
    COPY . .

    # Expose the port Flask runs on
    EXPOSE 5003

    # Set environment variables
    ENV FLASK_APP=app.py
    ENV FLASK_RUN_HOST=0.0.0.0

    # Optional to set different port instead of default port
    ENV FLASK_RUN_PORT=5003

    # Command to run the application
    CMD ["flask", "run"]
    ```

## Requirements

Make sure you have a `requirements.txt` file in the root of your project with the necessary dependencies:

    ```
    Flask==3.1.0
    numpy==2.0.1
    pandas==2.2.3
    scikit_learn==1.6.1
    ```

## Application Code

Ensure you have an `app.py` file in the root of your project with the Flask application code:

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
         return 'Hello, World!'

    if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5003) # Change the port here
    ```

