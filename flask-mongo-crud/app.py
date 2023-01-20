from flask import Flask, jsonify, request
from mongo_client import MongoDb
import os

app = Flask(__name__)
#mongo = MongoClient(os.environ.get('MONGO_HOST'), os.environ.get('MONGO_PORT'),username=os.environ.get('MONGO_INITDB_ROOT_USERNAME'),password=os.environ.get('MONGO_INITDB_ROOT_PASSWORD'))
mongo = MongoDb(db_name='crud',collection_name='poc1')

def get_headers():
    headers = {}
    headers['ip'] = request.headers.get('X-Real-IP', request.remote_addr)
    headers['user_agent'] = request.headers.get('User-Agent')
    headers['accept_language'] = request.headers.get('Accept-Language')
    headers['accept_encoding'] = request.headers.get('Accept-Encoding')
    headers['connection'] = request.headers.get('Connection')
    headers['host'] = request.headers.get('Host')
    return headers

@app.route('/')
def health_check():
    headers = get_headers()
    return jsonify(status="health", headers=headers)

@app.route('/api/get/<id>', methods=['GET'])
def get_by_id(id):
    doc = mongo.get_by_id(id)
    if doc:
        return jsonify(doc)
    else:
        return jsonify( {
                "status": "error",
                "message": "No ID was found" 
        }), 404
        

@app.route('/api/get', methods=['GET'])
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
    doc = mongo.update(data)
    return "Document updated", 200

@app.route('/api/delete/<id>', methods=['DELETE'])
def delete(id):
    mongo.delete(id)
    return "Document deleted", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)