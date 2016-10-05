#!/usr/bin/env python

import os
from flask import Flask, render_template, request, jsonify, session
from model import connect_to_db, db, User, Message


app = Flask(__name__)


@app.route('/')
def index_page():
    """Home page."""

    user = User.query.get(1)
    messages = Message.query.all()

    return render_template("index.html",
                           messages=messages,
                           user=user)


@app.route('/register')
def register_user():
    """Registration page."""

    return render_template("register.html")


@app.route('/process_registration', methods=['POST'])
def submit_registration():
    """Submit registration page."""

    email = request.form.get('email')
    password = hash(request.form.get('password'))
    location = request.form.get('location')
    role = request.form.getlist('role')

    return render_template("register.html",
                           email=email,
                           password=password,
                           location=location,
                           role=role)

if __name__ == "__main__":

    connect_to_db(app, os.environ.get("DATABASE_URL"))

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
