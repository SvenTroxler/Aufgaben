from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant_db"]
col = db["restaurants"]

pipeline = [
    {"$unwind": "$grades"},
    {
        "$group": {
            "_id": "$name",
            "avg_score": {"$avg": "$grades.score"}
        }
    },
    {"$sort": {"avg_score": -1}},
    {"$limit": 3}
]

ergebnisse = col.aggregate(pipeline)

for r in ergebnisse:
    print(f"{r['_id']}")