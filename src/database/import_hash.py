import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["hashes_database"]
collection = db["hash_collection"]

collection.insert_one({"hash": "af7ea2ae208c3c5377b41742c0d50c38294016ffa92e518d328fc2f10cfe4d00"})

print("Hash transferred successfully")
