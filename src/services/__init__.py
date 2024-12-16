# src/services/__init__.py

from src.services.database import get_data, update_data

def fetch_all_data():
    query = {}  # Define your query here
    return get_data(query)

def modify_data(query, data):
    return update_data(query, data)