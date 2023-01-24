from flask import Flask, request, jsonify
from mysql_client import UserService

app = Flask(__name__)

# Create an instance of the UserService
user_service = UserService()

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


# Create a user endpoint
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    user_service.create_user(name, email, password)

    return jsonify({"message": "User created"})

# Get user by ID endpoint
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)

    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

# Get all users endpoint
@app.route("/users", methods=["GET"])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users)

# Update user endpoint
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    user_service.update_user(user_id, name, email, password)

    return jsonify({"message": "User updated"})

# Delete user endpoint
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)