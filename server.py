#!/usr/bin/env python

import os
from flask import Flask, render_template, request, jsonify, session, redirect, flash
from model import connect_to_db, db, User, Message
from datetime import datetime


app = Flask(__name__)

app.secret_key = 'abc' # os.environ.get("FLASK_SECRET_KEY")


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
    confirmed_at = datetime.now()

    user = User(email=email,
                password=password,
                location=location,
                role=role,
                confirmed_at=confirmed_at)

    db.session.add(user)
    db.session.commit()

    session['logged_in'] = User.query.filter_by(email=email).one().user_id

    return render_template("user.html",
                           email=email,
                           password=password,
                           location=location,
                           role=role)


@app.route('/login')
def login():

    return render_template("login.html")


@app.route('/process_login', methods=['POST'])
def process_login():

    email = request.form.get('email')
    password = hash(request.form.get('password'))

    try:
        user = User.query.filter_by(email=email).one()

        if int(user.password) == password:
            session['logged_in'] = user.user_id

            return render_template("user.html",
                                   email=user.email,
                                   password=user.password,
                                   location=user.location,
                                   role=user.role)
        else:
            flash('Incorrect password.')
            return render_template("login.html")
    except:
        flash('Email not found.')
        return render_template("login.html")


@app.route('/logout')
def logout():

    if "logged_in" in session:
        del session['logged_in']

    return render_template("index.html")


if __name__ == "__main__":

    connect_to_db(app, os.environ.get("DATABASE_URL"))

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
