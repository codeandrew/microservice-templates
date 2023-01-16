from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/yourdbname"
mongo = PyMongo(app)

@app.route("/api/register", methods=["POST"])
def register():
    # Get the data from the request
    data = request.json
    # extract data from json
    username = data['username']
    password = data['password']
    name = data['name']
    email = data['email']

    # Check if the user already exists
    existing_user = mongo.db.users.find_one({"username": username})
    if existing_user:
        return jsonify({"status": "error", "message": "A user with that username already exists"})

    # Insert the user into the collection
    result = mongo.db.users.insert_one({
        "username": username,
        "password": password,
        "name": name,
        "email": email
    })
    # Return the result
    return jsonify({"status": "success", "id": str(result.inserted_id)})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    # extract data from json
    username = data['username']
    password = data['password']

    user = mongo.db.users.find_one({"username": username, "password": password})
    if user:
        return jsonify({"status": "success", "user": dumps(user)})
    else:
        return jsonify({"status": "error", "message": "Invalid username or password"})

@app.route("/api/account", methods=["POST"])
def account_setup():
    # Get the data from the request
    data = request.json
    # extract data from json
    user_id = data['user_id']
    profile_picture = data.get('profile_picture')
    bio = data.get('bio')

    # Find the user in the database
    user = mongo.db.users.find_one({"_id": user_id})
    if not user:
        return jsonify({"status": "error", "message": "User not found"})

    # Update the user's account details
    mongo.db.users.update_one({"_id": user_id}, {"$set": {"profile_picture": profile_picture, "bio": bio}})
    updated_user = mongo.db.users.find_one({"_id": user_id})

    # Return the updated user
    return jsonify({"status": "success", "user": dumps(updated_user)})

if __name__ == '__main__':
    app.run(debug=True)
