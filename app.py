from flask import Flask, send_from_directory
from flask_restful import Api
from playhouse.flask_utils import FlaskDB

app = Flask(__name__, static_url_path="", static_folder="public")
api = Api(app)


@app.route("/", defaults={"path": ""})
def serve(path):
    return send_from_directory(app.static_folder, path)
