from flask import Flask, jsonify
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/hello", methods=["GET"])
    def sample_route():
        return jsonify({"message": "This is a sample route"})

    return app
