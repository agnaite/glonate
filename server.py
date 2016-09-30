#!/usr/bin/env python

from environment import *
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)

@app.route('/')
def index_page():
    user = User.select().where(User.email == 'test@example.com').first()
    messages = Message.select().where(Message.user == user)

    return render_template("index.html",
                           messages=messages,
                           user=user)

if __name__ == "__main__":
    db.connect()
    app.run(debug=True)
