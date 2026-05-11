from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "CI/CD Demo."
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/tal", methods=["GET"])
def tal():
    return "working", 200


# ✅ 404 Not Found handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "You did something wrong,ב Fooyah!"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
