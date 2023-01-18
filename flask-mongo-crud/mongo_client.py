from bson.objectid import ObjectId
from pymongo import MongoClient
import os

class MongoDb:
    def __init__(self, db_name, collection_name):
        #self.client = MongoClient()
        self.client = MongoClient( os.environ.get('MONGO_HOST'), int(os.environ.get('MONGO_PORT')),username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'),password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'))
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get(self, _id):
        doc = self.collection.find_one({"_id": ObjectId(_id)})
        if doc:
            return self.serialize_doc(doc)
        else:
            return None

    def getAll(self):
        docs = self.collection.find()
        return [self.serialize_doc(doc) for doc in docs]

    def create(self, data):
        self.collection.insert_one(data)
        return self.serialize_doc(data)

    def update(self, _id, data):
        try:
            self.collection.update_one({"_id": ObjectId(_id)}, {"$set": data})
            return self.serialize_doc(data)
        except:
            return {"status": "error"}


    def delete(self, _id):
        try:
            self.collection.delete_one({"_id": ObjectId(_id)})
            return {"status": "success"}
        except:
            return {"status": "error"}

    def serialize_doc(self, doc):
        doc["_id"] = str(doc["_id"])
        return doc
