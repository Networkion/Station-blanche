from time import sleep
import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["hashes_database"]
collection = db["hash_collection"]

with open("./src/database/hashes.txt", "r") as file:
    hashes = file.readlines()

for hash_str in hashes:
    hash_value = hash_str.strip()
    if hash_value:  # Vérifier si la ligne n'est pas vide
        collection.insert_one({"hash": hash_value})
        sleep(5)

print("Transfert des hachages terminé avec succès.")