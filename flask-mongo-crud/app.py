from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from mongo_client import MongoDb
import os

app = Flask(__name__)
CORS(app)
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
@cross_origin()
def get_by_id(id):
    doc = mongo.get_by_id(id)
    if doc:
        return jsonify(doc)
    else:
        return jsonify({
                "status": "error 404",
                "message": "No ID was found" 
        }), 404

@app.route('/api/get', methods=['GET'])
@cross_origin()
def get_all():
    docs = mongo.get_all()
    return jsonify(docs)

@app.route('/api/create', methods=['POST'])
@cross_origin()
def create():
    data = request.get_json()
    response = mongo.create(data)
    return jsonify(response), 201

@app.route('/api/update/<id>', methods=['PUT'])
@cross_origin()
def update(id):
    data = request.get_json()
    doc = mongo.update(id, data)
    print(doc)
    return jsonify(doc),200
    # if doc:
    #     # response = {
    #     #     "status": "Document updated",
    #     #     "doc": doc
    #     # }
    #     # return response, 200
    #     return jsonify(doc),200
    # else:
    #     return jsonify({
    #             "status": "error 404",
    #             "message": "No ID was found" 
    #     }), 404

@app.route('/api/delete/<id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    doc = mongo.delete(id)
    if doc: 
        return { "status": "Document deleted" }, 200
    else:
        return jsonify({
                "status": "error",
                "message": "No ID was found" 
        }), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
