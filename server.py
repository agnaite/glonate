from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)

@app.route('/')
def index_page():
    """Show index page."""

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
