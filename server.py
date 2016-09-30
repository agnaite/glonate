#!/usr/bin/env python

import datetime

from flask import Flask, render_template, request, jsonify, session

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

app = Flask(__name__)

db = SqliteExtDatabase('my_database.db')

class BaseModel(Model):
    ''' basic peewee setup '''
    class Meta:
        database = db


class User(BaseModel):
    email = CharField(unique=True)


class Message(BaseModel):
    user = ForeignKeyField(User, related_name='messages')
    body = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)


@app.route('/')
def index_page():
    user = User.select().where(User.email << 'test@example.com')
    messages = [ Message.select().where(Message.user << user) ]
    print(messages)

    return render_template("index.html",
                           messages=messages,
                           usage=user)

if __name__ == "__main__":
    db.connect()
    db.create_tables([User, Message])
    user = User.create(email='test@example.com')
    message = Message.create(user=user, body='human gives money. human receives money. human glonates')
    app.run()
