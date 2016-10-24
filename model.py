# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

####################################################################
# Model definitions


class User(db.Model):
    """User. A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # User authentication information
    password = db.Column(db.String, nullable=False)

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # User information
    image = db.Column(db.String(264), server_default='https://medium.com/img/default-avatar.png')
    role = db.Column(db.String(264))
    location = db.Column(db.String(264))


class Message(db.Model):
    """Message. A user has many messages."""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime())


def example_data():
    """Create some sample data."""

    user = User(password="abc",
                email="jane@example.com",
                confirmed_at=datetime.datetime.now(),
                role="donor",
                location="Germany")

    messenger = User(password="abc",
                     email="tom@example.com",
                     confirmed_at=datetime.datetime.now(),
                     role="messenger",
                     location="India")

    msg1 = Message(user=user.user_id, body='human needs money', created_at=datetime.datetime.now())
    msg2 = Message(user=messenger.user_id, body='human gives money', created_at=datetime.datetime.now())
    msg3 = Message(user=user.user_id, body='human says ty', created_at=datetime.datetime.now())
   
    db.session.add_all([user, messenger, msg1, msg2, msg3])

    db.session.commit()


####################################################################
# Helper functions


def connect_to_db(app, db_uri=None):
    """Connect the database to the Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///glonate'
    app.config['SQLALCHEMY_ECHO'] = True
    
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    import os
    connect_to_db(app, os.getenv('DATABASE_URL'))

    # Create our tables and some sample data
    db.create_all()
    example_data()

    print "Connected to DB."
