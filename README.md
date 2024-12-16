# Flask REST API with MongoDB

This project is a Flask-based REST API that interacts with a MongoDB database. It provides endpoints for GET and PUT requests to manage data.

## Project Structure

```
flask-rest-api
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── controllers           # Contains business logic for API endpoints
│   ├── models                # Defines MongoDB data models
│   ├── routes                # Sets up API routes
│   └── services              # Contains database interaction logic
├── Dockerfile                 # Docker configuration for the application
├── requirements.txt           # Python dependencies
├── kubernetes                # Kubernetes deployment and service configurations
│   ├── deployment.yaml       
│   └── service.yaml          
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd <project dir>
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   python src/app.py
   ```

## API Usage

- **GET /api/resource**: Retrieve data from the MongoDB database.
- **PUT /api/resource**: Update data in the MongoDB database.

## Docker Instructions

1. **Build the Docker image:**
   ```
   docker build -t flask-rest-api .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 5000:5000 flask-rest-api
   ```

## Kubernetes Deployment

1. **Deploy the application:**
   ```
   kubectl apply -f kubernetes/deployment.yaml
   ```

2. **Expose the service:**
   ```
   kubectl apply -f kubernetes/service.yaml
   ```

## License

This project is licensed under the MIT License.