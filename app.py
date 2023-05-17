from flask import Flask
from routes.pages import page

app = Flask(__name__)

app.register_blueprint(page)

if __name__ == "__main__":
    app.run(port=8000, debug=True)