from flask import Flask, jsonify, request
from mongo_client import MongoDb
import os

app = Flask(__name__)
#mongo = MongoClient(os.environ.get('MONGO_HOST'), os.environ.get('MONGO_PORT'),username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'),password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'))
mongo = MongoDb(db_name='crud',collection_name='poc1')

@app.route('/')
def health_check():
    return jsonify(status="health")

@app.route('/api/get/<id>', methods=['GET'])
def get_by_id(id):
    doc = mongo.get(id)
    if doc:
        return jsonify(doc)
    else:
        return "Document not found", 404

@app.route('/api/getall', methods=['GET'])
def get_all():
    docs = mongo.get_all()
    return jsonify(docs)

@app.route('/api/create', methods=['POST'])
def create():
    data = request.get_json()
    response = mongo.create(data)
    return jsonify(response), 201

@app.route('/api/update', methods=['PUT'])
def update():
    data = request.get_json()
    mongo.update(data)
    return "Document updated", 200

@app.route('/api/delete/<id>', methods=['DELETE'])
def delete(id):
    mongo.delete(id)
    return "Document deleted", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)