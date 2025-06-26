#!/usr/bin/env python3
"""
    basic Flask app
"""
from auth import Auth
from flask import Flask, request, jsonify


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """GET / endpoint"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """
    POST /users endpoint to register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
