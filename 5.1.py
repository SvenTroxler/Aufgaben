from datetime import datetime
from time import sleep
import psutil
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
col = client["monitoring"]["power"]

class Power:
    def __init__(self, cpu=None, ram_total=None, ram_used=None, timestamp=None, _id=None):
        if _id is not None:
            self._id = _id
        
        if cpu is None:
            self.cpu = psutil.cpu_percent()
            self.ram_total = psutil.virtual_memory().total
            self.ram_used = psutil.virtual_memory().used
            self.timestamp = datetime.now()
        else:
            self.cpu = cpu
            self.ram_total = ram_total
            self.ram_used = ram_used
            self.timestamp = timestamp

while True:
    p = Power()
    col.insert_one(p.__dict__)
    print(f"{p.timestamp} | CPU: {p.cpu}% | RAM: {p.ram_used}/{p.ram_total}")

    count = col.count_documents({})
    if count > 10000:
        oldest = col.find().sort("timestamp", 1).limit(count - 10000)
        ids = [doc["_id"] for doc in oldest]
        col.delete_many({"_id": {"$in": ids}})

    sleep(1)