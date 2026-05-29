from pymongo import MongoClient
from joke import Joke

class Dao_joke:
    def __init__(self, connection_string):
        self.col = MongoClient(connection_string)["jokes"]["jokes"]

    def insert(self, joke):
        self.col.insert_one(joke.__dict__)

    def get_category(self, category):
        results = self.col.find({"category": category})
        return [Joke(**doc) for doc in results]

    def delete(self, id):
        import bson
        self.col.delete_one({"_id": bson.ObjectId(id)})