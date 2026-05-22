from pymongo import MongoClient

# Verbindung herstellen
client = MongoClient("mongodb://localhost:27017/")

# Datenbank und Collection selektieren (Namen ggf. anpassen!)
db = client["restaurant_db"] 
collection = db["restaurants"] 

stadtbezirke = collection.distinct("borough")

# Ausgabe
for bezirk in stadtbezirke:
    print(bezirk)