from flask import Flask
from flask_cors import CORS
from db import create_tables
from routes import init_routes
import os

app = Flask(__name__)
CORS(app)

create_tables()

@app.route("/")
def index():
    return "SMX Norway API"

init_routes(app)

if __name__ == "__main__":
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=8000, debug=debug)
