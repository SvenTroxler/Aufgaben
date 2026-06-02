from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant_db"]
col = db["restaurants"]

for bezirk in col.distinct("borough"):
    print(bezirk)