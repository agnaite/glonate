#!/usr/bin/env python

from environment import *
import os
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)


@app.route('/')
def index_page():
    user = User.select().where(User.email == 'test@example.com').first()
    messages = Message.select()

    return render_template("index.html",
                           messages=messages,
                           user=user)

if __name__ == "__main__":
    db.connect()

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(port=PORT, debug=DEBUG)
