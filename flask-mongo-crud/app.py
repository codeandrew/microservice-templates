from flask import Flask, jsonify, request
from mongo_client import MongoClient

app = Flask(__name__)
mongo = MongoClient()

@app.route('/get/<id>', methods=['GET'])
def get_by_id(id):
    doc = mongo.get(id)
    if doc:
        return jsonify(doc)
    else:
        return "Document not found", 404

@app.route('/getall', methods=['GET'])
def get_all():
    docs = mongo.get_all()
    return jsonify(docs)

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    mongo.create(data)
    return "Document created", 201

@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    mongo.update(data)
    return "Document updated", 200

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    mongo.delete(id)
    return "Document deleted", 200

if __name__ == '__main__':
    app.run()
