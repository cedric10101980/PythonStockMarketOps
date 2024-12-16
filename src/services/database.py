from pymongo import MongoClient, errors

client = MongoClient("mongodb://localhost:27017/")
db = client["flask_rest_api_db"]
collection = db["items"]

def get_data(query):
    try:
        return list(collection.find(query))
    except errors.ServerSelectionTimeoutError as e:
        return {"error": "Database connection failed", "details": str(e)}
    except Exception as e:
        return {"error": "An error occurred while fetching data", "details": str(e)}

def update_data(query, data):
    try:
        result = collection.update_one(query, {'$set': data})
        if result.matched_count == 0:
            return {"error": "No matching document found"}
        return {"status": "Item updated"}
    except errors.ServerSelectionTimeoutError as e:
        return {"error": "Database connection failed", "details": str(e)}
    except Exception as e:
        return {"error": "An error occurred while updating data", "details": str(e)}