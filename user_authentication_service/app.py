#!/usr/bin/env python3
"""
    basic Flask app
"""
from auth import Auth
from flask import Flask, request, jsonify, abort, make_response, redirect


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


@app.route('/session', methods=['POST'])
def login() -> str:
    '''session endpoint'''
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


@app.route('/session', methods=['DELETE'])
def logout() -> str:
    """
        DELETE /sessions endpoint to logout a user
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect("/")


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """
        Get profile endpoint to get user profile
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)
    return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
