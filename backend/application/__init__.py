from flask import Flask, request, jsonify
from flask_cors import CORS
import openai


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    CORS(app)

    @app.post("/")
    def index():
        if (
            "history" not in request.json
            or not request.json["history"]
        ):
            return jsonify({
                "status": 401,
                "message": {
                    "message": "invalid request"
                }
            })

        if (
            "openai_api_key" not in request.json
            or not request.json["openai_api_key"]
        ):
            return jsonify({
                "status": 201,
                "message": {
                    "openai_api_key": "cannot be empty"
                }
            })

        openai.api_key = request.json["openai_api_key"]

        history = request.json["history"]

        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history
            )
        except Exception as e:
            return jsonify({
                "status": 201,
                "message": {
                    "openai_api_key": e.error.message
                }
            })

        ans = resp.choices[0].message.content
        history.append(
            {
                "role": "assistant",
                "content": ans,
            }
        )

        return jsonify({
            "status": 200,
            "message": "successful",
            "data": {
                "history": history
            }
        })

    return app
