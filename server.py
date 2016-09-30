from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index_page():
    """Show index page."""

    messages = ['human gives money', 'human receives money', 'human glonates']

    return render_template("index.html",
                           messages=messages)

if __name__ == "__main__":

    # user = User('test', 'test@example.com')
    # db.session.add(user)
    # db.session.commit()
    # db.create_all()
    app.run(debug=True)
