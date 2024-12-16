from flask import Flask, request, jsonify
from pymongo import MongoClient
from src.routes import api_routes
from urllib.parse import quote

from src.services.stocks import fetch_and_store_mutual_fund_data

app = Flask(__name__)

# Register routes
app.register_blueprint(api_routes)

@app.route('/')
def home():
    return "Welcome to the Flask REST API!"

@app.route('/fetch-mutual-fund-data', methods=['GET'])
def fetch_mutual_fund_data():
    try:
        fetch_and_store_mutual_fund_data()
        return jsonify({"message": "Data fetched and stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)