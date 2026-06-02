from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant_db"]
col = db["restaurants"]

while True:
    suche = input("Restaurantname: ")
    results = list(col.find({"name": {"$regex": suche, "$options": "i"}}))

    if not results:
        print("Nichts gefunden.")
        continue

    for i, r in enumerate(results):
        print(f"[{i}] {r['name']} ({r['borough']}, {r['cuisine']})")

    auswahl = input("Auswahl: ")
    if not auswahl.isdigit() or int(auswahl) >= len(results):
        print("Ungueltige Eingabe.")
        continue

    restaurant = results[int(auswahl)]
    print(f"Ausgewaehlt: {restaurant['name']}")

    note = input("Note (A/B/C): ").upper()
    if note not in ["A", "B", "C"]:
        print("Ungueltige Note.")
        continue

    col.update_one(
        {"_id": restaurant["_id"]},
        {"$push": {"grades": {
            "date": datetime.now(),
            "grade": note
        }}}
    )

    print("Gespeichert.")