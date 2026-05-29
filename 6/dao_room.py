from pymongo import MongoClient
from room import Room

class Dao_room:
    def __init__(self, connection_string):
        self.col = MongoClient(connection_string)["buildings"]["rooms"]

    def create(self, room):
        self.col.insert_one(room.__dict__)

    def read(self):
        return Room(**self.col.find_one())

    def update(self, name, updates):
        self.col.update_one({"name": name}, {"$set": updates})

    def delete(self, name):
        self.col.delete_one({"name": name})