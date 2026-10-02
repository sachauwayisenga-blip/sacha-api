from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "name": "SACHA API",
        "status": "online",
        "message": "Welcome to SACHA API!"
    })


@app.route("/api")
def api_info():
    return jsonify({
        "name": "SACHA API",
        "version": "1.0",
        "services": [
            "chat",
            "image",
            "video"
        ]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )