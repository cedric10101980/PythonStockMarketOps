from src.services import fetch_all_data, modify_data

def get_items():
    return fetch_all_data()

def update_item(query, data):
    return modify_data(query, data)