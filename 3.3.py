from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant_db"]
col = db["restaurants"]

perigord = col.find_one({"name": "Le Perigord"})
coords = perigord["address"]["coord"]

col.create_index([("address.coord", "2d")])

result = col.find_one({
    "address.coord": {
        "$near": coords
    },
    "name": {"$ne": "Le Perigord"}
})

print(result["name"])