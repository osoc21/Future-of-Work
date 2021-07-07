from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/api/test", methods=["GET"])
    def sample_route():
        return jsonify({"message": "This is a sample route"})

    return app
