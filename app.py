from flask import Flask
import sqlite3
from routes.api import api

app = Flask(__name__)

def get_db():
    con = sqlite3.connect('./data/database/wikidata.db')
    con.row_factory = sqlite3.Row
    return con

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(port=8000, debug=True)