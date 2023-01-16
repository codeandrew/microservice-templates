from pymongo import MongoClient

class MongoDb:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get(self, _id):
        doc = self.collection.find_one({"_id": _id})
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
        self.collection.update_one({"_id": _id}, {"$set": data})
        return self.serialize_doc(data)

    def delete(self, _id):
        self.collection.delete_one({"_id": _id})

    def serialize_doc(self, doc):
        doc["_id"] = str(doc["_id"])
        return doc
