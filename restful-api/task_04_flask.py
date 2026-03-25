#!/usr/bin/python3
"""
Simple Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory
users = {}


@app.route("/", methods=["GET"])
def home():
    """Home endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """API status"""
    return "OK"


@app.route("/data", methods=["GET"])
def get_data():
    """Return all usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user by username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add new user"""

    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()
